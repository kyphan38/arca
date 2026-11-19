---
name: lesson
description: Start or finish one lesson for any topic in docs/ (AWS, Kubernetes, Terraform, Vault, ...) using the source registry - course videos with .srt transcripts, doc pages, or books. Start - find the lesson, create an empty note from the template with the header filled, and give 2-3 questions to watch for. Done - compare the user's note with the source, list missed or wrong facts, then run the /cards flow and update 00-map.md. Never writes the note content. Use when the user says they will study a lesson, video, or doc page, has finished one, or runs /lesson.
argument-hint: [topic] <lesson number, words, or URL> | done [note.md]
allowed-tools: Bash(python3 *)
---

# Lesson

Arguments: `$ARGUMENTS`

- Optional topic first (`aws`, `k8s`) - a key from the Sources table. Without it, use the topic of the last lesson in this conversation, else the topic whose `00-map.md` has a `doing` row and changed most recently. If still unclear, ask
- Then a lesson number (`264`), words from its title (`dead letter`), or a URL - Start
- `done`, optionally with a note path - Done. Without a path, use the note created by the last Start in this conversation, else the most recently changed note under `docs/`

Script: `S=.claude/skills/lesson/scripts/srt.py` (run from the repo root)

## Sources

One row per topic being studied. To start a new topic, ask the user for the source, add a row here, and update the study method page (`docs/00-introduction/study-method.md`)

| Key | Topic folder | Source | Kind | Location | Header | Traps heading |
| --- | --- | --- | --- | --- | --- | --- |
| aws | `docs/02-technologies/aws/` | Adrian Cantrill SAA-C03 | videos + srt | `/Users/kyphan/Documents/courses/aws/` | `> Cantrill <number> · <date>` | Exam Traps |

Kinds

- `videos + srt` - a folder of `NNNN_Title.mp4` + `.srt`. Find with `find`, read with `text` and `hints`
- `docs` - official doc pages or blog posts. The lesson argument is a URL, or a page title to search for. Read the page with WebFetch
- `book` - no text to compare. Start works, Done skips the compare step and goes to cards

Notes on the `aws` source

- Flat folder, no section folders. Lesson numbers mostly follow the course order, but late `update_ch_...` lessons (e.g. 0383-0385) belong to earlier sections - place them by topic, not by number
- Transcripts are machine-made (Whisper), so they have hearing errors - "dead letter cues" for queues, "NQ timestamp" for enqueue timestamp. When the note and the transcript disagree on a name or term, use the real AWS term and do not report it as the user's mistake

## Golden Rule

The source is for checking, never for writing. Claude does not put any fact from the source into the note file - not as bullets, not as fill-in blanks, not as hints. The user writes everything after `## Problem` from memory

## Start

1. Find the lesson
   - `videos + srt` - `python3 $S find <location> <query>`
   - `docs` - the URL, or search the official docs for the title and confirm the page with the user
   - Several matches - list them and ask which one
   - Multi-part lessons (`PART1`, `PART2`) share one note. If the note for another part already exists, use it and add the new lesson number to its header
2. Read the source - `python3 $S text <file>` and `python3 $S hints <file>`, or the doc page
3. Decide the note
   - Section folder - from the topic's `00-map.md` (latest `doing` row). If it is not clear, ask the user. Create the folder only if missing
   - File name - kebab-case title without the number and course tags (`SHAREDALL`, `ASSOCIATESHARED`, `EXTRA`, `YYYYMMUPDATE` like `202204UPDATE`, `PART1`, `Demo`), e.g. `0264_SQS_Dead_Letter_Queues` → `sqs-dead-letter-queues.md`
   - A note on the same topic already exists - do not make a second file, add the lesson to the existing one
4. Demo or lab lesson (`Demo` or `DEMO` in the name, or a hands-on tutorial page) - do not create a note. Tell the user to do it, clean up after, then add a `Lab Log` (3 lines) to the related note
5. Create the note from `scripts/templates/note.md`
   - Frontmatter - `title` = the H1, `sidebar_position` = next number in the section folder, `tags` = topic key plus course key (e.g. `[aws, aws-saa]`)
   - Leave `description` empty - the user writes one line after the lesson, in their own words
   - H1 - the lesson title, lowercase
   - Header - from the Sources table, or `> <source> - <URL or chapter> · <date>`
   - Keep every section empty. Keep the template comments
   - Rename `Traps` to the Traps heading from the Sources table
6. Reply in chat, short - nothing of this goes into the file
   - The note path
   - Prerequisites - if the source says to study another lesson first, name it and say if a note for it exists
   - 2-3 questions to keep in mind while studying. Ask about the problem and the "why", not details. Do not answer them
   - The reminder - finish the lesson, close it, then write from memory

## Done

1. Read the note and the source (`text` and `hints`, or the doc page). Kind `book` - skip to step 4
2. Compare and report in chat, grouped
   - Wrong - facts in the note that the source contradicts
   - Missed and important - what the source stresses (exam, important, careful, numbers, limits, defaults) that the note lacks
   - Missed but minor - one line, or skip
   - Do not report wording or style
3. Do not edit the note body. The user adds the missed facts in their own words
   - Offer to rewatch hints - the rough position in the lesson for each missed fact, if it helps
4. When the user has updated the note, run the `/cards` steps on it - coverage check by question type, draft gaps, approve, preview, push
5. Update the topic's `00-map.md` - add the note link to its section row, create the row if needed (status `doing`)
6. One-line summary - note path, cards added, what is next (the next lesson number)
