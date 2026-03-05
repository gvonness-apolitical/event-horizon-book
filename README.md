# Event Horizon

**A Computational Journey into Black Hole Physics**

A LaTeX textbook teaching the physics, mathematics, and numerical methods behind the [event-horizon](https://github.com/gvonness/event-horizon) relativistic ray tracer and numerical relativity engine. Written by Greg von Nessi.

## Table of Contents

### Part I: Foundations
1. Special Relativity
2. Differential Geometry
3. General Relativity

### Part II: Black Holes
4. Schwarzschild Black Holes
5. Kerr Black Holes
6. Geodesics

### Part III: Numerical Methods
7. Finite Differences
8. ODE Integration
9. Automatic Differentiation
10. Spectral Methods

### Part IV: Numerical Relativity
11. ADM Decomposition
12. BSSN & CCZ4
13. Initial Data
14. Adaptive Mesh Refinement
15. Wave Extraction
16. Horizons
17. Binary Black Holes

### Part V: General-Relativistic Magnetohydrodynamics
18. Ideal MHD
19. GRMHD
20. Accretion

### Part VI: Visualization and Rendering
21. Ray Tracing
22. Camera and Rendering
23. Colour Science

### Part VII: Advanced Topics
24. Discontinuous Galerkin Methods

**Appendices:** Notation, Numerical Primer, Codebase Map

## Building the PDF

**Requirements:** TeX Live 2024+ with LuaLaTeX, latexmk, biber

**macOS:**
```bash
brew install --cask mactex
```

**Build:**
```bash
make        # Build PDF → build/book.pdf
make clean  # Remove build artifacts
make watch  # Continuous rebuild on file changes
```

## Project Structure

```
src/
├── book.tex              # Root document
├── ehbook.cls            # Document class
├── ehcommands.tex        # Shared macros
├── references.bib        # Bibliography
├── frontmatter/          # Title page, preface
├── part1_foundations/     # Chapters 1–3
├── part2_black_holes/    # Chapters 4–6
├── part3_numerical_methods/  # Chapters 7–10
├── part4_numerical_relativity/  # Chapters 11–17
├── part5_grmhd/          # Chapters 18–20
├── part6_visualization/  # Chapters 21–23
├── part7_advanced/       # Chapter 24
└── appendices/           # Notation, numerical primer, codebase map
figures/                  # Shared figures and matplotlib helpers
```

## Companion Codebase

The companion code is at [github.com/gvonness/event-horizon](https://github.com/gvonness/event-horizon) (Haskell + Rust).

## Status

Work in progress.
