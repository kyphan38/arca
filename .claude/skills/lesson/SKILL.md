---
name: lesson
description: Start or finish one course lesson from its .srt transcript. Start - find the lesson by number or words, create an empty note from the template with the header filled, and give 2-3 questions to watch for. Done - compare the user's note with the transcript, list missed or wrong facts, then run the /cards flow and update 00-map.md. Never writes the note content. Use when the user says they will study a lesson or video, has finished one, or runs /lesson.
argument-hint: <lesson number or words> | done [note.md]
allowed-tools: Bash(python3 *)
---

# Lesson

Arguments: `$ARGUMENTS`

- A lesson number (`264`, `0264`) or words from its title (`dead letter`) - Start
- `done`, optionally with a note path - Done. Without a path, use the note created by the last Start in this conversation, else the most recently changed note under `docs/`

Video folder: `/Users/kyphan/Documents/courses/aws/` - flat, one `NNNN_Title.mp4` + `.srt` per lesson, no section folders (change this line if the course files move)

Script: `S=.claude/skills/lesson/scripts/srt.py` (run from the repo root)

## Golden Rule

The transcript is for checking, never for writing. Claude does not put any fact from the transcript into the note file - not as bullets, not as fill-in blanks, not as hints. The user writes everything after `## Problem` from memory

## Start

1. Find the lesson - `python3 $S find <video folder> <query>`
   - Several matches - list them and ask which one
   - Multi-part lessons (`PART1`, `PART2`) share one note. If the note for another part already exists, use it and add the new lesson number to its header
2. Read the transcript - `python3 $S text <file>` and `python3 $S hints <file>`
3. Decide the note
   - Topic - which `docs/<category>/<topic>/` (e.g. `docs/02-technologies/aws/`)
   - Section folder - from the topic's `00-map.md` (latest `doing` row). If it is not clear, ask the user. Create the folder only if missing
   - File name - kebab-case title without the number and course tags (`SHAREDALL`, `ASSOCIATESHARED`, `EXTRA`, `YYYYMMUPDATE` like `202204UPDATE`, `PART1`, `Demo`), e.g. `0264_SQS_Dead_Letter_Queues` → `sqs-dead-letter-queues.md`
   - A note on the same topic already exists - do not make a second file, add the lesson to the existing one
4. Demo lesson (`Demo` or `DEMO` in the name) - do not create a note. Tell the user to do the demo, then add a `Lab Log` (3 lines) to the related note
5. Create the note from `scripts/templates/note.md`
   - H1 - the lesson title, lowercase
   - Header - `> Cantrill <number> · <today>`
   - Keep every section empty. Keep the template comments
   - Cert courses (AWS) - rename `Traps` to `Exam Traps`
6. Reply in chat, short - nothing of this goes into the file
   - The note path
   - Prerequisites - if `hints` shows the teacher says to watch another lesson first, name it and say if a note for it exists
   - 2-3 questions to keep in mind while watching. Ask about the problem and the "why", not details. Do not answer them
   - The reminder - watch fully, close the video, then write from memory

## Done

1. Read the note and the transcript (`text` and `hints`)
2. Compare and report in chat, grouped
   - Wrong - facts in the note that the transcript contradicts
   - Missed and important - what the teacher stresses (exam, important, careful, numbers, limits, defaults) that the note lacks
   - Missed but minor - one line, or skip
   - Do not report wording or style
3. Do not edit the note body. The user adds the missed facts in their own words
   - Offer to rewatch hints - the rough position in the lesson for each missed fact, if it helps
4. When the user has updated the note, run the `/cards` steps on it - coverage check by question type, draft gaps, approve, preview, push
5. Update the topic's `00-map.md` - add the note link to its section row, create the row if needed (status `doing`)
6. One-line summary - note path, cards added, what is next in the folder (the next lesson number)
