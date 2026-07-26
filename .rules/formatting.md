# System Instructions

- You are helping maintain a personal knowledge base built with Docusaurus
- When asked to write, rewrite, or format any note, always apply the rules below - no exceptions
- These rules apply to all `.md` files in the `docs/` directory
- When asked to "format", "rewrite", or "clean up" any note, apply these rules
- Follow the exact rules defined in the `arca/scripts` folder
- Ensure that running `scripts/main.py` or `scripts/lint.py` passes

## Style

- Concise and direct - cut every word that doesn't add meaning
- Note-taking style, not essay style
- No filler phrases: "In this section", "As we can see", "It is important to note", "Concepts are", "Categories are", "Examples are", etc
- Prefer bullet points for facts, lists, comparisons
- Use prose only when a concept genuinely needs a sentence to make sense
- Simple vocabulary - if a simpler word works, use it
- Fix grammar and spelling errors silently
- Strictly follow standard Markdown formatting
- Do not use a period (.) at the end of sentences (exception: abbreviations like etc.)
- Do not use a colon (:) even when introducing a list

## Conciseness

Principle: cut words, not facts. If removing a phrase doesn't change meaning, remove it. If removing loses a fact, condition, or reason, keep it

### Always cut

- Filler openers - "As we know", "It is worth noting", "In this section", "To understand better"
- Redundant hedges - "perhaps", "generally", "usually" when not expressing real uncertainty
- Throat-clearing - "Before diving in", "First of all"
- Duplicate info - if a fact already appears in a bullet above, do not repeat
- Adjective stacking - "very important and necessary" → "important"

### Never cut

- Conditions - "when X then Y" - keep both X and Y
- Exceptions - "except when", "unless"
- Numbers, names, versions, dates
- Causal links - "because", "therefore", "leads to"
- Trade-offs - "in exchange", "however", "downside"

### Rewrite patterns

- Long verb phrase → single verb
  - "perform a check on" → "check"
  - "has the ability to" → "can"
- Nominalization → verb
  - "the implementation faces difficulties" → "implementation is hard"
- Passive → active when subject is clear
- "X is a Y that Z" → "X - Y, Z" or two separate bullets

### Sentence length

- Prose sentence - max 20 words. Longer → split or convert to bullet
- Bullet - max 15 words. Longer → split into two bullets or sub-bullets
- Prose block - max 3 consecutive sentences. Longer → bulletize

### Format conversion priority

When reformatting a raw note, prefer in this order

1. Single fact → bullet
2. List of 2+ items in same category → bullet group
3. Compare/contrast → table or paired bullets
4. Process/sequence → numbered list
5. Definition → "term - definition" on one line
6. Prose only when needed for causal chains or nuance

### When in doubt

If a raw sentence is ambiguous, do not guess and rewrite. Keep the original and flag it

```markdown
<!-- UNCLEAR: does this mean X or Y? -->
```

Preserving unclear intent is better than producing clean but wrong output

## File Structure

Every markdown file must follow this exact order

```markdown
# title in all lowercase

- [ ] Progress: Draft/Review/Done

## Section One

...

## Section Two

...
```

### Rules

- H1 - all lowercase, exactly one per file, first line
- Second line - `- [ ] Progress: Draft/Review/Done` - use Draft for new notes
- H2/H3 - Title Case (first letter uppercase)
- Max depth - H3 - never use H4, H5, H6

### Section Names

Section names (H2/H3) are freestyle and flexible. For recommended reference section titles, see `scripts/headings_reference.txt`.

## What NOT to Do

- Do not add sections or content not present in the raw notes
- Do not use bold for emphasis inside sentences - use it only for key terms in definitions
- Do not summarize unless explicitly asked
- Do not wrap output in code fences unless it's actually code
- Do not change image paths, table content, or code blocks

## Examples

### Example 1 - cut filler

Raw

> It is worth noting that when we use Docker, we can see that building images often takes quite a lot of time, especially when we have many layers in the Dockerfile

Formatted

- Docker build is slow when Dockerfile has many layers

### Example 2 - keep facts, cut words

Raw

> Redis can be used as a cache layer in front of the database, which helps reduce load on the database and increase response speed, however we need to be aware of cache invalidation issues when data changes

Formatted

- Redis as cache in front of DB - reduces DB load, increases response speed
- Trade-off - cache invalidation when data changes

### Example 3 - split long sentence into bullets

Raw

> A JWT token consists of 3 parts which are header, payload and signature, where header contains algorithm info, payload contains claims, and signature is used to verify integrity

Formatted

- JWT - 3 parts - header, payload, signature
  - Header - algorithm
  - Payload - claims
  - Signature - verify integrity

### Example 4 - do NOT cut when information is lost

Raw

> PostgreSQL supports JSONB since version 9.4, faster than JSON because it stores binary, but uses slightly more disk

Bad (loses info)

- PostgreSQL supports JSONB, faster than JSON

Good

- PostgreSQL JSONB (since 9.4) - faster than JSON due to binary storage
- Trade-off - uses more disk than JSON