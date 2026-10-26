---
name: cards
description: Turn notes in docs/ into Anki cards through AnkiConnect - `## Questions` lines and filled `Note` cells in problem-list tables. First checks which question types the note covers (fundamental, scenario, interview, traps) and drafts missing ones for the user to approve. Use when the user asks for flashcards or runs /cards.
argument-hint: <note.md or folder> [deck]
allowed-tools: Bash(python3 *)
---

# Cards

Arguments: `$ARGUMENTS`

- First argument: a note, or a folder (every `.md` in it except `00-map.md`). If missing, ask which note
- Deck, if given. Default `arca::<topic>` from the path, e.g. `docs/02-technologies/aws/...` → `arca::aws`

Script: `S=.claude/skills/cards/scripts/cards.py` (run from the repo root)

## Question Types

Every note should be covered by these, in this priority

| Type | Tests | Example shape |
| --- | --- | --- |
| Fundamental | Why it exists, how it works step by step | "Why does X exist?", "Walk through what happens when ..." |
| Scenario | Picking the right tool for a need (cert exams) | "A company needs ... Which option?" |
| Interview | Explaining, trade-offs, comparing, debugging | "X vs Y - when each?", "Downside of ...?", "Z keeps failing - what do you check?" |
| Traps | Limits, defaults, numbers, gotchas | "What happens to ... when ...?", "Max size of ...?" |

- Every note needs at least 1-2 Fundamental cards. The others depend on the topic
  - Cert course (AWS) - Scenario and Traps matter most after Fundamental
  - Tools (Docker, Linux) - Interview and Traps
  - Theory (game theory, algorithms) - Fundamental and Interview
- Skip trivia - yes/no questions, console click paths, facts you would just look up
- One fact per card. Answer short enough to say out loud in 10 seconds

## Rules

- Cards live in the note first, Anki second. Every card is a `- Q: ... A: ...` line under `## Questions`
- Use only facts in the note
  - A good question that needs a fact outside the note may be proposed, marked "(not in your note)"
  - If the user accepts it, they add that fact to the note body too
- Problem-list tables (leetcode) - each filled `Note` cell becomes a card "(problem) - which pattern, and why?"
  - Skip the coverage check for these tables. If a note is long or is a full solution, say so

## Steps

1. Read the note
2. Coverage check - show a short table, type → questions that already cover it (by line), and what is missing
   - Also list facts in `Traps` and `How It Works` that no question covers
   - Flag weak questions (trivia, yes/no, two facts in one card) with a better version
3. Draft new or improved `- Q: ... A: ...` lines for the gaps, labeled by type. Show them, and write them into `## Questions` only after the user says yes (they may edit them)
   - If a fact in the note looks wrong, say so - do not fix it silently
4. Preview: `python3 $S <notes> [--deck "<deck>"] --dry-run`
   - Fix any `SKIP` lines in the note (wrong form), then preview again
5. Push: `python3 $S <notes> [--deck "<deck>"]`
   - Cards already in the deck are skipped, so running it again is safe
   - If AnkiConnect is not reachable, tell the user to open Anki and stop
6. Report in one line - cards added, deck
