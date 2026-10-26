"""Find course lessons by number or words, and read their .srt as plain text.

  python3 srt.py find <dir> <query>...
      List lessons whose file name matches a number (264, 0264) or all the words.
  python3 srt.py text <file.srt>...
      Print the transcript as one block of text per file (no numbers, no timestamps).
  python3 srt.py hints <file.srt>...
      Print only sentences where the teacher stresses something - exam, important,
      required, careful, remember, prerequisites.
"""
import argparse
import os
import re
import sys

TIME = re.compile(r"-->")
NUM = re.compile(r"^\d+$")
HINT = re.compile(
    r"\b(exam|important|required|need to (know|understand|remember)|be aware|careful|remember|"
    r"haven't watched|watch .* first|prerequisite|default|maximum|minimum|limit)\b",
    re.IGNORECASE,
)


def text_of(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = [l.strip() for l in f if l.strip() and not NUM.match(l.strip()) and not TIME.search(l)]
    return re.sub(r"\s+", " ", " ".join(lines)).strip()


def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", text) if s.strip()]


def cmd_find(a):
    if not os.path.isdir(a.dir):
        sys.exit(f"Video folder not found: {a.dir}")
    files = sorted(f for f in os.listdir(a.dir) if f.lower().endswith(".srt"))
    q = " ".join(a.query)
    if q.isdigit():
        hits = [f for f in files if re.match(r"^0*(\d+)", f) and int(re.match(r"^0*(\d+)", f).group(1) or 0) == int(q)]
    else:
        words = [w.lower() for w in a.query]
        hits = [f for f in files if all(w in f.lower().replace("_", " ") for w in words)]
    if not hits:
        sys.exit(f"No lesson matches '{q}' in {a.dir}")
    for f in hits:
        print(os.path.join(a.dir, f))


def cmd_text(a):
    for p in a.files:
        print(f"== {os.path.basename(p)}\n{text_of(p)}\n")


def cmd_hints(a):
    for p in a.files:
        print(f"== {os.path.basename(p)}")
        for s in sentences(text_of(p)):
            if HINT.search(s):
                print(f"- {s}")
        print()


def main():
    p = argparse.ArgumentParser()
    s = p.add_subparsers(dest="cmd", required=True)
    f = s.add_parser("find")
    f.add_argument("dir")
    f.add_argument("query", nargs="+")
    f.set_defaults(fn=cmd_find)
    for name, fn in (("text", cmd_text), ("hints", cmd_hints)):
        t = s.add_parser(name)
        t.add_argument("files", nargs="+")
        t.set_defaults(fn=fn)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
