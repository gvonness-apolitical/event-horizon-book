---
name: draft-section
description: "Draft LaTeX prose for a single section of the event-horizon-book, following the IFI cycle and tonal reference."
argument-hint: <chapter-path> [section-label] [--no-review]
---

# /draft-section

Draft LaTeX prose for a single section following the Intuition–Formalism–Intuition cycle.

## Interface

```
/draft-section <chapter-path> [section-label] [--no-review]
```

- `chapter-path`: relative to `src/` (e.g., `part2_black_holes/ch06_geodesics`)
- `section-label`: optional (e.g., `sec:geo-null`); if omitted, draft the chapter introduction and first section
- `--no-review`: optional flag to skip the editorial board (Steps 7–10) for fast iteration
- If the chapter stub has no `\section{}` entries, draft only the chapter introduction and note this in the output

## Process

### Step 1 — Load Context

Read the following files in parallel:

| File | Path |
|------|------|
| Tonal reference | `src/tone.md` |
| Target chapter | `src/{chapter-path}/chapter.tex` |
| Shared macros | `src/ehcommands.tex` |
| Document class | `src/ehbook.cls` |
| Bibliography | `src/references.bib` |
| Continuity tracker | `src/continuity.md` (may not exist on first use — proceed without it) |

### Step 2 — Load Surrounding Context

From `src/book.tex`, identify the previous and next chapters relative to the target. Read both chapter stubs. Also read:

- `src/appendices/notation.tex` (if it exists)
- Any chapters explicitly referenced in the target stub's description (e.g., via `\cref`)

### Step 3 — Load Codebase Context

Parse `\coderef{Module}{Symbol}` entries from the **entire chapter stub** (not just the target section — sibling sections establish module context). Map module paths to source files:

- **Haskell:** `\coderef{Module.Sub}{Symbol}` → `/Users/gvn/Dev/Entrolution/event-horizon/src/EventHorizon/Module/Sub.hs`
- **Rust:** `\coderef{crate_name}{file.rs}` → `/Users/gvn/Dev/Entrolution/event-horizon/rust/{crate_name}/src/{file}.rs`
- **WGSL:** `\coderef{crate_name}{file.wgsl}` → `/Users/gvn/Dev/Entrolution/event-horizon/rust/{crate_name}/src/{file}.wgsl`

Read each resolved source file. If a source file is not found at the expected path, note this in the output and proceed without it.

### Step 4 — Identify Section Scope

From the chapter stub, extract for the target section:

- Title and label
- Description text (the stub paragraph)
- Position in chapter (which section number, what comes before and after)
- Existing `\coderef` entries
- Whether the section has `\starmark` (optional/advanced)

### Step 5 — Draft the Section

Write LaTeX prose following the IFI cycle from `tone.md`. Include:

- **Introducing sentence** before every displayed equation
- **Interpreting sentence** after every displayed equation
- `\label{eq:...}` on all displayed equations
- `\coderef{}{}` margin notes at first encounter of codebase-implemented concepts
- **Figure placeholders** with description, source type, parameters, draft caption, and label (see tone.md §5)
- **Margin notes** (`\physnote`, `\implnote`, `\histnote`, `\xrefnote`, `\warnnote`) where appropriate
- `\cite{}` references — flag missing bibliography keys as `\cite{TODO:AuthorYear}`
- Use macros from `ehcommands.tex` consistently (never raw `g_{\mu\nu}` when `\metric` exists)
- Use `\cref{}` for all cross-references

### Step 6 — Self-Review Checklist

Before presenting the output, verify:

- [ ] No anti-patterns from tone.md §8 (no "well known", "easily shown", "obviously", section-heading echo, "in this section we will")
- [ ] Every displayed equation has introducing and interpreting prose
- [ ] No more than 3 consecutive displayed equations without prose
- [ ] All `ehcommands.tex` macros used where applicable
- [ ] British English spelling throughout (colour, behaviour, generalise)
- [ ] Label conventions followed (`eq:`, `fig:`, `sec:`, `thm:`)
- [ ] At least one figure placeholder for sections with geometric or numerical content
- [ ] Opening sentence does not repeat the section heading
- [ ] `\starmark` sections do not assume the reader has read other `\starmark` sections

### Step 7 — Spawn Editorial Board

**Skip conditions:** Skip Steps 7–10 entirely if:
- This is a **chapter introduction** (no `section-label` argument — these are 2–3 paragraphs, too short to warrant 4 specialist reviews)
- The user passed `--no-review`

Read the four reviewer prompt files from `prompts/` relative to this skill:
- `prompts/physicist.md`
- `prompts/mathematician.md`
- `prompts/pedagogy.md`
- `prompts/continuity.md`

**Spawn 4 `general-purpose` agents in parallel** using the Agent tool. Each agent receives:
1. Its reviewer prompt (from the file above)
2. The full draft section text (inline in the prompt)
3. Role-specific context files (inline in the prompt or instructed to read)

**Context distribution per reviewer:**

| Reviewer | Context (beyond draft) |
|----------|------------------------|
| Physicist | `ehcommands.tex`, chapter stub, codebase source files from Step 3 (max 3 files, truncated to relevant functions/types) |
| Applied Mathematician | `ehcommands.tex`, chapter stub |
| Pedagogy Specialist | `tone.md` (full file), chapter stub |
| Continuity Specialist | `continuity.md`, `tone.md`, `ehcommands.tex`, up to 3 most recent preceding drafted sections in same chapter, adjacent chapter stubs (previous and next from Step 2) |

Each reviewer must return their review in the structured format defined in their prompt file. If a reviewer fails to return or returns malformed output, proceed with available reviews. **Minimum quorum: 2 of 4 reviewers must return valid reviews to proceed.**

### Step 8 — Editor Synthesis (Round 1)

The lead agent acts as **chief technical editor**. Process all returned reviews:

1. Read all reviews (require minimum 2)
2. Classify each issue: **ACCEPT** / **REJECT** (with reason) / **CONFLICT**
3. Resolve conflicts using judgement; physics correctness and mathematical rigour serve as default tiebreakers when the editor has no strong view
4. If accepting a correction conflicts with a reviewer's **Preserve** note, document the justification for overriding the Preserve
5. Apply all accepted corrections to the draft
6. If any **MAJOR** issues were accepted → proceed to Step 9 (Round 2)
7. Otherwise → skip to Step 11

### Step 9 — Conditional Round 2

**Skip if:** All reviewers returned PASS or MINOR verdicts, or no MAJOR issues were accepted in Step 8.

Re-submit the revised draft to **only the reviewers who raised MAJOR issues** (not all 4). Spawn agents in parallel as in Step 7, but with a modified prompt:

> "You previously reviewed this section and raised MAJOR issues. The draft has been revised. Verify your MAJOR issues are addressed. Report only remaining MAJOR issues using the same review format. Do not raise new issues."

Process returned reviews. If a reviewer does not return, proceed without them.

### Step 10 — Final Editorial Pass

1. Apply remaining corrections from Round 2 or make final unilateral calls
2. Round 2 ignores any newly raised issues not present in Round 1
3. Unresolved disagreements go to the output's "Open questions" section with the editor's rationale
4. Regenerate continuity notes from the post-review (final) draft, not the pre-review draft

**Hard limit: 2 review-revise rounds total.** After Round 2, the editor makes all final decisions.

### Step 11 — Write Files, Build, and Fix Overflows

**Write the section file:**

- Path: `src/{chapter-path}/{label-suffix}.tex`, where `{label-suffix}` is the section label with the `sec:` prefix removed (e.g., `sec:sr-minkowski` → `sr-minkowski.tex`)
- The file starts with a comment `% sec:label — Section Title`, then `\section{...}`, `\label{...}`, and the full section content
- For chapter introductions (no section-label argument): write the introduction directly into `chapter.tex`, replacing the existing stub paragraph

**Update the chapter file:**

- Replace the section's stub block (from `\section{...}` through the stub paragraph, including any `\coderef` line) with `\input{chapter-path/label-suffix}`
- Keep a `% ---- Stubs (to be drafted) ----` comment before the first remaining stub if one doesn't exist
- Preserve all other sections, the Key References block, and the chapter introduction

**Build and fix overfull hboxes:**

- Run `make` to compile the PDF
- Check the build log for `Overfull \hbox` warnings in the newly written section file (filter by the section's filename in the log). Ignore warnings from other chapters.
- For each overfull hbox, identify the offending line from the log context (LaTeX shows the problematic text), then fix the source:
  - Long inline maths → move to a displayed equation
  - Long compound words or words jammed against em-dashes → reword for better line breaks
  - Margin notes stacking/colliding → move the `\marginnote` call to a later paragraph
- Rebuild and repeat until there are zero overfull hbox warnings from the new section
- If an overfull hbox is less than 1pt, it can be ignored

**Present the following to the user:**

1. **Section summary** — 2-3 sentences on what was drafted and key choices made
2. **Continuity notes** — always produce these (regenerated from post-review draft if editorial board ran), even on first invocation:
   - Notation introduced (symbols, where defined)
   - Analogies used (what they map, where they break)
   - Forward references made (promises to fulfil in later sections)
   - Backward references used (callbacks to earlier material)
3. **Missing references** — bibliography keys used but not in `references.bib`
4. **Figure specifications** — detailed specs for each placeholder
5. **Editorial board summary** (omit if editorial board was skipped):
   - Verdicts: `Physicist: PASS, Mathematician: MINOR, Pedagogy: MINOR, Continuity: MAJOR` (example)
   - Round 2: whether triggered, which reviewers, and outcome
   - Corrections applied: count and brief list
   - Corrections rejected: count with reasons
   - Conflicts resolved: count with rationale
   - When all reviewers return PASS: "Editorial board: all PASS, no corrections applied."
6. **Open questions** — anything requiring author decision, including unresolved editorial disagreements from Step 10

## Guidelines

### Do

- Follow the IFI cycle for every section
- Use specific numbers to ground abstractions (masses, radii, timescales)
- Show all derivation steps with justification
- Connect to the codebase with `\coderef` and code excerpts
- Write substantial figure captions (3–5 sentences, self-contained)
- Check that cross-reference targets (`\cref{sec:...}`) exist in the chapter stub
- Distinguish between `\starmark` and non-`\starmark` content

### Don't

- Draft more than one section at a time
- Invent citation keys — use `\cite{TODO:AuthorYear}` for missing ones
- Use `\subsubsection` — use `\paragraph{}` for finer structure
- Include full source files — excerpt 5–15 lines maximum
- Assume the reader has read `\starmark` sections in earlier chapters
- Use American English (color, behavior, generalize)

### Length

- **Section:** 800–2000 words (shorter for narrow technical sections, longer for foundational ones)
- **Chapter introduction:** 2–3 paragraphs expanding the stub description
