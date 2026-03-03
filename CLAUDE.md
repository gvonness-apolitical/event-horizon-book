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
- `src/partN_name/chNN_name/chapter.tex` — Chapter files
- `figures/` — Shared figures and images

## Adding a Chapter

1. Create directory: `src/partN_name/chNN_name/`
2. Create `chapter.tex` in that directory
3. Add `\include{partN_name/chNN_name/chapter}` to `src/book.tex`

## Conventions

- **LuaLaTeX only** — do not use pdfLaTeX-specific packages or commands
- Use macros from `ehcommands.tex` for consistency
- The star symbol marks optional or advanced sections

## Related Codebase

The companion code repository is at github.com/gvonness/event-horizon (Haskell + Rust).
