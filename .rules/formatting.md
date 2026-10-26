# System Instructions

- You are helping maintain a personal knowledge base built with Docusaurus
- Goal - the user learns and remembers. Pretty notes are not the goal
- These rules apply to all `.md` files in the `docs/` directory
- Ensure that running `scripts/lint.py` passes - it checks kebab-case names, one H1, max depth H3

## Who Writes What

- The user writes the notes, in their own words, after watching or reading the source
- Claude does not write or rewrite note content unless the user asks for that exact note
- Claude's job - ask questions, check notes against the source, find gaps, make flashcards (`/lesson`, `/cards`, `/quiz`)
- `/lesson` may create an empty note from the template, but never puts facts from the source into it
- When checking a note, point out wrong or missing facts - do not polish the wording
- Vietnamese, English, or a mix are all fine - keep technical terms in English

## Study Method Page

- `docs/00-introduction/study-method.md` - the user's guide to the whole repo and study flow, all topics. Always write it in Vietnamese
- Whenever you change `.rules/`, `.claude/skills/`, or `scripts/templates/`, update that page in the same change so it matches - steps, skill names, arguments, sections, decks, sources

## Never Delete

- Never delete a note or "start a topic over", even if the user asks to clean up
- Old or messy notes stay - fix them in place, or move them to an `_archive/` folder (Docusaurus and the linter skip `_` paths)
- If the user wants to restart a topic after a break, point them to `/quiz comeback` first

## Note Format

- Template - `scripts/templates/note.md`
- Example - `docs/02-technologies/aws/13-serverless-and-application-services/sqs-dead-letter-queues.md`
- Sections - `Problem`, `How It Works`, `Traps`, `Questions` - skip a section if it has nothing
  - Cert courses may call it `Exam Traps`
  - Other section names are fine when the topic needs them
- One H1 on the first line, max depth H3
- About 40 lines per note - longer usually means copying the source
- Max 1 image per note - a self-drawn diagram or a Mermaid block beats a screenshot of slides
- Demo or lab lessons - no note needed, or 3 lines in the related note (what I did, what broke, the fix)

## Questions Section

- One card per bullet - `- Q: question A: answer`
- `/cards` turns these lines into Anki cards, so every fact worth remembering must end up here
- Prefer "why" and scenario questions over plain definitions
- Problem-list tables (e.g. leetcode) - a filled `Note` cell also becomes a card. A trailing `(redo)` marks a problem to re-solve and is left out of the card
  - Front - the problem, back - the note
  - Write the recognition hint (which pattern and why), not the full solution

## Folders

- Topic folder - `docs/<category>/<topic>/`, e.g. `docs/02-technologies/aws/`
- Inside a course, name folders after course sections, e.g. `13-serverless-and-application-services`
- Create a folder only when starting that section - no empty placeholder folders
- Optional `00-map.md` per topic - one line per section with its status, update it when a section starts or ends

## When Asked To Rewrite

Only when the user asks to format, rewrite, or clean up a specific note

- Cut words, not facts
- Always cut - filler openers, throat-clearing, duplicate info, adjective stacking
- Never cut - conditions, exceptions, numbers, names, versions, dates, causal links, trade-offs
- Prefer bullets for facts and lists, tables for comparisons, numbered lists for steps
- Keep the user's voice and language - do not turn it into textbook style
- Do not add content that is not in the note
- Do not change image paths, table content, or code blocks
- Do not use the em dash - use a plain hyphen with spaces ( - ) instead

If a sentence is ambiguous, keep the original and flag it - do not guess

```markdown
<!-- UNCLEAR: does this mean X or Y? -->
```

### Example - keep facts, cut words

Raw

> Redis can be used as a cache layer in front of the database, which helps reduce load on the database and increase response speed, however we need to be aware of cache invalidation issues when data changes

Formatted

- Redis as cache in front of DB - reduces DB load, increases response speed
- Trade-off - cache invalidation when data changes

### Example - do not cut when information is lost

Raw

> PostgreSQL supports JSONB since version 9.4, faster than JSON because it stores binary, but uses slightly more disk

Bad (loses info)

- PostgreSQL supports JSONB, faster than JSON

Good

- PostgreSQL JSONB (since 9.4) - faster than JSON due to binary storage
- Trade-off - uses more disk than JSON
