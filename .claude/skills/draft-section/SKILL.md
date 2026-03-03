---
name: draft-section
description: "Draft LaTeX prose for a single section of the event-horizon-book, following the IFI cycle and tonal reference."
argument-hint: <chapter-path> [section-label]
---

# /draft-section

Draft LaTeX prose for a single section following the Intuition–Formalism–Intuition cycle.

## Interface

```
/draft-section <chapter-path> [section-label]
```

- `chapter-path`: relative to `src/` (e.g., `part2_black_holes/ch06_geodesics`)
- `section-label`: optional (e.g., `sec:geo-null`); if omitted, draft the chapter introduction and first section
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

### Step 7 — Write Files, Build, and Fix Overflows

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
2. **Continuity notes** — always produce these, even on first invocation:
   - Notation introduced (symbols, where defined)
   - Analogies used (what they map, where they break)
   - Forward references made (promises to fulfil in later sections)
   - Backward references used (callbacks to earlier material)
3. **Missing references** — bibliography keys used but not in `references.bib`
4. **Figure specifications** — detailed specs for each placeholder
5. **Open questions** — anything requiring author decision

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
