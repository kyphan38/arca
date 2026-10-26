---
name: quiz
description: Quiz the user on notes in docs/ - Claude asks fundamental, scenario, interview and trap questions one at a time, the user answers in their own words, Claude grades against the note and records gaps as new questions. Also the comeback routine after a study break. Use when the user asks to be quizzed or tested, says they are back after a break, or runs /quiz.
argument-hint: [note, folder, or "comeback" [topic]] [interview]
---

# Quiz

Arguments: `$ARGUMENTS`

- A note or a folder under `docs/` - quiz on that
- `comeback` (optional topic) - run the comeback routine below
- `interview` - mock interview mode, see below
- No argument - quiz on the notes changed most recently (`git log --name-only -- docs`), or the latest `doing` section of a topic's `00-map.md`

## Question Mix

Same types as `/cards` - Fundamental, Scenario, Interview, Traps

- Start with 2 Fundamental questions. If the user cannot explain the basics, stay on basics
- Then mix the rest by topic - cert courses lean Scenario and Traps, tools and theory lean Interview
- Interview questions are open - "explain X to a junior", "X vs Y", "what breaks if ...", "how would you debug ..."
- Do not just read back the note's `## Questions` lines. Rephrase them or ask from a new angle, so the user cannot pass on memorized wording

## Rules

- Ask one question at a time, then wait for the answer. Never show the answer before the user tries
- Grade against the note. Outside facts only to point out a likely gap, marked "(not in your note)"
- Short feedback - right / partly / wrong, the missing piece, one line
- Talk in the language the user answers in. Keep technical terms in English
- Never suggest deleting notes or starting a topic over

## Steps

1. Read the notes for the scope
2. Ask 5-8 questions, one by one
3. At the end
   - Score by type, e.g. Fundamental 2/2, Scenario 1/3, Interview 1/2
   - Weakest type - one line on what to practice
   - Questions missed or half right - offer to add them to that note's `## Questions` as `- Q: ... A: ...` lines. Write only after the user says yes
   - Wrong facts in the note itself - list them for the user to fix
   - Suggest `/cards` for notes that got new questions

## Interview Mode

- 3-4 open questions, mostly Interview type, with one follow-up each ("why?", "what if load is 10x?")
- Grade the answer like an interviewer - correct, clear, mentions trade-offs
- At the end, show a short model answer for the weakest question

## Comeback Routine

For when the user returns after a break and feels they forgot everything

1. Say clearly - do not delete, do not restart. Forgetting is normal, relearning is faster than first learning
2. Ask them to clear the Anki `arca` backlog first (cap at 100 reviews per day if it is huge)
3. Find the last 2 sections they studied (topic `00-map.md`, or `git log -- docs`). Quiz 4 Fundamental questions on each
4. Each missed topic - give the note path and the source lesson from its header. Revisit only those
5. Then continue with the next new lesson as normal
