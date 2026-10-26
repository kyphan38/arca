"""Notes in docs/ -> Anki Basic cards, through AnkiConnect.

  python3 cards.py <note.md>... [--deck D] [--dry-run]
      Read `- Q: ... A: ...` lines under `## Questions`, and filled `Note` cells
      in problem-list tables, then add the new cards to Anki.
      Default deck: arca::<topic>, from docs/<category>/<topic>/...
      --dry-run prints the cards and which are new, without changing Anki.
"""
import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

ANKI_URL = "http://127.0.0.1:8765"
MODEL = "Basic"
QA = re.compile(r"^\s*-\s*Q:\s*(.+?)\s+A:\s*(.+?)\s*$")
CODE = re.compile(r"`([^`]+)`")
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
NUM_PREFIX = re.compile(r"^\d+-")


def anki(action, **params):
    body = json.dumps({"action": action, "version": 6, "params": params}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(ANKI_URL, body), timeout=30) as r:
            res = json.load(r)
    except urllib.error.URLError:
        sys.exit("Cannot reach AnkiConnect. Open Anki and make sure the AnkiConnect add-on is installed.")
    if res.get("error"):
        raise RuntimeError(f"AnkiConnect {action}: {res['error']}")
    return res["result"]


def fmt(text):
    return CODE.sub(r"<code>\1</code>", html.escape(text, quote=False))


def topic_of(path):
    # docs/<category>/<topic>/... -> topic, docs/<category>/<file>.md -> file
    parts = os.path.normpath(os.path.abspath(path)).split(os.sep)
    rest = parts[len(parts) - parts[::-1].index("docs"):] if "docs" in parts else parts[-1:]
    name = rest[1] if len(rest) >= 3 else os.path.splitext(rest[-1])[0]
    return NUM_PREFIX.sub("", name)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_note(path):
    cards, bad = [], []
    in_q, note_col, prev = False, None, ""
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            if line.startswith("## "):
                in_q = line.strip() == "## Questions"
            elif line.lstrip().startswith("|"):
                row = cells(line)
                if all(set(c) <= set("-: ") for c in row):
                    # Separator row: the previous line was the header
                    head = [c.lower() for c in cells(prev)]
                    note_col = head.index("note") if "note" in head else None
                elif note_col is not None and len(row) > note_col and row[note_col]:
                    title = LINK.sub(r"\1", row[0])
                    # "(redo)" is the user's re-solve marker, not part of the answer
                    answer = re.sub(r"\s*\(redo\)\s*$", "", row[note_col])
                    cards.append({"q": f"{title} - which pattern, and why?", "a": answer, "line": n})
            else:
                note_col = None
                if in_q and line.strip():
                    m = QA.match(line)
                    if m:
                        cards.append({"q": m.group(1), "a": m.group(2), "line": n})
                    elif line.lstrip().startswith("-"):
                        bad.append((n, line.rstrip()))
            prev = line
    return cards, bad


def note(card, deck, path):
    stem = os.path.splitext(os.path.basename(path))[0]
    topic = topic_of(path)
    back = f'{fmt(card["a"])}<br><br><small>{html.escape(topic)} / {html.escape(stem)}</small>'
    return {
        "deckName": deck,
        "modelName": MODEL,
        "fields": {"Front": fmt(card["q"]), "Back": back},
        "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        "tags": ["arca", f"arca::{topic}::{stem}"],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("notes", nargs="+")
    p.add_argument("--deck", help="Override the default arca::<topic> deck")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    notes = []
    for path in a.notes:
        cards, bad = parse_note(path)
        for n, line in bad:
            print(f"SKIP {path}:{n} not in '- Q: ... A: ...' form: {line}")
        deck = a.deck or f"arca::{topic_of(path)}"
        notes += [(c, note(c, deck, path), path) for c in cards]

    if not notes:
        sys.exit("No cards found - no '- Q: ... A: ...' lines and no filled 'Note' cells")

    if a.dry_run:
        try:
            ok = anki("canAddNotes", notes=[n for _, n, _ in notes]) if MODEL in anki("modelNames") else [True] * len(notes)
        except SystemExit:
            ok = [None] * len(notes)
        for (c, n, path), new in zip(notes, ok):
            state = "?" if new is None else ("new" if new else "exists")
            print(f"[{state}] {n['deckName']}  {os.path.basename(path)}:{c['line']}  Q: {c['q']}  A: {c['a']}")
        return

    if MODEL not in anki("modelNames"):
        sys.exit(f"Note type '{MODEL}' not found in Anki")
    for deck in sorted({n["deckName"] for _, n, _ in notes}):
        anki("createDeck", deck=deck)
    ok = anki("canAddNotes", notes=[n for _, n, _ in notes])
    new = [x for x, keep in zip(notes, ok) if keep]
    if new:
        anki("addNotes", notes=[n for _, n, _ in new])
    print(f"Added {len(new)} new cards, skipped {len(notes) - len(new)} already there")
    for c, n, path in new:
        print(f"  + {n['deckName']}  {os.path.basename(path)}:{c['line']}  {c['q']}")


if __name__ == "__main__":
    main()
