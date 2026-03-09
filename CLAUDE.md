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
- **Figure captions** must include a short caption for the List of Figures: `\caption[Short title]{Full caption...}`

## Related Codebase

The companion code repository is at github.com/gvonness/event-horizon (Haskell + Rust).

<!-- MEMORY_START -->
## Memory Context

## Recent Context
- [09/03/2026] [Assistant] I now have everything needed for a thorough pedagogical review. Here is my assessment:  ---  ## Pedagogical Review: Section 10.6 — LGL Differentiation and Mass Lumping  ### Verdict: **MINO...
- [09/03/2026] [User] You are a technical writing and cross-chapter consistency specialist reviewing a draft section for notation consistency, continuity, and conventions.  ## Your scope  You check **continuity, not...
- [09/03/2026] [Assistant] Now I have all the information I need. Let me compile the review.  ---  ## Continuity Review: `sec:spec-lgl`  ### MAJOR Issues  1. **Notation inconsistency: `$\ell_j'(x_i)$` vs registry `$...

## Last Session (05/03/2026 01:44)
- [Assistant] Now I have all the information needed to perform a rigorous mathematical review. Let me verify each formula systematically.  **Formula 1: ...
- [User] You are a science and mathematics pedagogy specialist reviewing a draft section of a graduate-level textbook for pedagogical effectiveness.  ##...

### Drafting Black Hole Sections
This conversation cluster is about a user working with a tool to draft sections related to black holes, covering topics like Kerr horizons, geodesics, and Schwarzschild coordinates.

### Lorentz Transformations and Observer Tetrads
This topic cluster is about the Lorentz group, which describes the allowed coordinate transformations between different inertial observers in special relativity. It also discusses how observer tetrads, constructed from four vectors, generalize the local frame of an observer to curved spacetime.

---
*Memory summary: 2 topics, 3 recent items, last session included*

<!-- MEMORY_END -->
