# Event Horizon Book

LaTeX textbook teaching the physics, mathematics, and numerical methods behind the event-horizon relativistic ray tracer and numerical relativity engine.

## Build

```bash
make        # Build PDF (output: build/book.pdf)
make clean  # Remove build artifacts
make watch  # Continuous rebuild on file changes
```

**Requirements:** TeX Live 2024+ with LuaLaTeX, latexmk, biber

**macOS install:**
```bash
brew install --cask mactex
```

## Project Structure

- `src/book.tex` — Root document
- `src/ehbook.cls` — Document class
- `src/ehcommands.tex` — Shared macros and commands
- `src/references.bib` — Bibliography database
- `src/tone.md` — Tonal reference for AI-assisted drafting
- `src/continuity.md` — Notation/analogy/reference tracker across sections
- `src/partN_name/chNN_name/chapter.tex` — Chapter file (intro + `\input{}` for drafted sections, stubs inline for undrafted)
- `src/partN_name/chNN_name/label-suffix.tex` — Drafted section files (e.g., `sr-minkowski.tex`)
- `figures/` — Shared figures, matplotlib style, and plot helper
- `.claude/skills/draft-section/` — Section drafting skill

## Adding a Chapter

1. Create directory: `src/partN_name/chNN_name/`
2. Create `chapter.tex` in that directory
3. Add `\include{partN_name/chNN_name/chapter}` to `src/book.tex`

## Section File Convention

Each drafted section lives in its own `.tex` file alongside `chapter.tex`. The filename is the section label with the `sec:` prefix removed (e.g., `sec:sr-minkowski` → `sr-minkowski.tex`). The chapter file `\input{}`s drafted sections and keeps undrafted stubs inline. Use `/draft-section` to draft sections.

## Conventions

- **LuaLaTeX only** — do not use pdfLaTeX-specific packages or commands
- Use macros from `ehcommands.tex` for consistency
- The star symbol marks optional or advanced sections

## Related Codebase

The companion code repository is at github.com/gvonness/event-horizon (Haskell + Rust).

<!-- MEMORY_START -->
## Memory Context

## Recent Context
- [03/03/2026] [User] I'm redesigning the draft-section skill for a LaTeX textbook project. The current skill has a single agent that drafts, self-reviews, and outputs. The new design adds an **editorial board** of ...
- [03/03/2026] [Assistant] Now I have a thorough understanding of the entire project. Let me construct the detailed implementation plan.  ---  ## Implementation Plan: Editorial Board Review for `/draft-section`  ###...
- [03/03/2026] [User] You are a plan critic. Read the plan at `/Users/gvn/.claude/plans/happy-hopping-manatee.md` and identify genuine improvements. The plan is for revising a LaTeX textbook drafting skill to includ...

## Last Session (03/03/2026 22:37)
- [User] Thoroughly explore the draft-section skill and its supporting infrastructure. I need to understand:  1. The full content of the skill definitio...
- [Assistant] Perfect. I now have complete context. Let me provide you with a comprehensive summary of all the files:  ---  ## Comprehensive Exploration...

### GRMHD Solver Development
This conversation cluster is about the development and debugging of a general relativistic magnetohydrodynamics (GRMHD) solver, including the implementation of key components such as the curved spacetime metric, conversion between conservative and primitive variables, source term computations, and testing of a torus initialization and evolution.

---
*Memory summary: 1 topics, 3 recent items, last session included*

<!-- MEMORY_END -->
