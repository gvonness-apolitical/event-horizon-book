# Tonal Reference — Event Horizon

This document codifies the voice, teaching method, and prose conventions for *Event Horizon: A Computational Journey into Black Hole Physics*. It is read by Claude during `/draft-section` invocations and is not compiled by LaTeX.

The primary tonal model is David MacKay's *Information Theory, Inference, and Learning Algorithms* — a book that is simultaneously rigorous, intuitive, and honest about difficulty. The voice is the author's: systematic, precise, direct, analogy-driven, and respectful of the reader's intelligence.

---

## 1. Voice and Register

Write as a colleague at a whiteboard, not a lecturer reading from notes. The reader is a capable person who chose to pick up this book — treat them accordingly.

**Register:** Conversational but precise. First person plural ("we derive", "we see that"). Contractions are fine in prose ("doesn't", "we'll"), though not in formal definitions or theorem statements. British English throughout (colour, behaviour, metres, generalise, grey).

**Humour:** Through understatement and precision, never through jokes, exclamation marks, or forced enthusiasm. If something is genuinely surprising, let the mathematics do the surprising.

**Directness:** No hedging, filler, or apologies for difficulty. If a derivation is hard, say it's hard and explain why — don't pretend it's easy or apologise for including it. "This is the most involved derivation in the chapter" is fine. "We apologise for the complexity" is not.

**NOT this voice:**
- Lecture transcript ("And so, as we can see on the slide...")
- Wikipedia article (neutral, third-person, citation-heavy prose without teaching)
- Feynman pastiche (folksy, digressive, performance-oriented)
- Graduate monograph (dense, notation-heavy, proof-theorem-proof with no motivation)

---

## 2. Teaching Method — The IFI Cycle

Every section follows the Intuition–Formalism–Intuition (IFI) cycle, adapted from MacKay's approach:

### Phase 1: Motivate (Intuition)

Open with *why* the reader should care. What problem does this concept solve? What goes wrong without it? Ground the motivation in something concrete — a physical scenario, a failure mode, a question the codebase must answer.

Good: "A naive integrator will cheerfully march your photon straight through the event horizon and out the other side. The Hamiltonian formulation prevents this by construction."

Bad: "In this section we discuss the Hamiltonian formulation of geodesic motion."

### Phase 2: Formalise (Mathematics)

Derive with all steps shown. Every intermediate step is justified — if a step isn't worth showing, say what was skipped and why. Notation is introduced before it is used. Equations build on each other; the reader should be able to follow with pen and paper.

### Phase 3: Interpret (Intuition)

After the derivation, explain what we proved and what it means. Connect back to the motivating question. Connect to the codebase — which module implements this, and how does the mathematical structure appear in the code? State the key insight in plain language.

### Metacognitive Signposting

Use margin notes to signal what kind of content the reader is encountering:
- `\physnote{}` — physics insight or physical interpretation
- `\implnote{}` — implementation detail or codebase connection
- `\histnote{}` — historical context
- `\xrefnote{}` — cross-reference to another chapter or section
- `\warnnote{}` — common pitfall or subtle point

These replace inline meta-commentary ("as we discussed in Chapter 3"). The margin note says it; the prose stays focused.

### Honest Difficulty

If a topic is hard, say so. If a derivation requires patience, set expectations at the start. If a concept has subtleties that trip up researchers, flag them. MacKay does this well — he tells you when something is going to be tricky, and that honesty builds trust.

---

## 3. Mathematics and Prose Integration

Mathematics is the backbone of this book. Prose is its companion, not its replacement. Every equation earns its place by being introduced, derived, and interpreted.

### The Equation Sandwich

Every displayed equation is preceded by a sentence that introduces it and followed by a sentence that interprets it. No orphan equations.

**Good:**
> The Hamiltonian for a free particle in curved spacetime takes a particularly clean form:
> \begin{equation}
>   \mathcal{H} = \tfrac{1}{2}\,\inversemetric\, p_\mu\, p_\nu \,.
>   \label{eq:geodesic-hamiltonian}
> \end{equation}
> For null geodesics, $\mathcal{H} = 0$ identically — this constraint is preserved exactly by Hamilton's equations, which makes it an excellent diagnostic for numerical accuracy.

**Bad:**
> \begin{equation}
>   \mathcal{H} = \tfrac{1}{2}\,g^{\mu\nu}\, p_\mu\, p_\nu
> \end{equation}
> \begin{equation}
>   \dot{x}^\mu = \frac{\partial \mathcal{H}}{\partial p_\mu}
> \end{equation}
> \begin{equation}
>   \dot{p}_\mu = -\frac{\partial \mathcal{H}}{\partial x^\mu}
> \end{equation}

### Consecutive Equation Limit

No more than three consecutive displayed equations without intervening prose. If a derivation naturally chains more than three, insert interpretation — what have we established so far? what's the next step?

### Derivation Steps

All steps are justified. If a step uses an identity, state the identity (or reference where it was derived). If a step is algebraic manipulation, say "expanding" or "collecting terms". If a step is non-obvious, explain the reasoning.

### Macro Consistency

Use macros from `ehcommands.tex` throughout: `\metric`, `\inversemetric`, `\christoffel{}{}{}`, `\lapse`, `\shift`, `\fourvel`, `\detmetric`, `\d`, `\order{}`, etc. Never write raw `g_{\mu\nu}` when `\metric` exists. This ensures consistent notation across the book and makes global changes possible.

### Notation Introduction

Introduce notation before using it. The first occurrence of a symbol gets an explicit definition: "$p_\mu$ denotes the covariant four-momentum". If notation was introduced in a previous chapter, either briefly remind the reader or use an `\xrefnote{}` margin note pointing to the definition.

### Worked Examples

At least one worked example per chapter (Parts I–IV). Use specific numbers — "for a Schwarzschild black hole of mass $M = 10\,M_\odot$" rather than "for a black hole". Worked examples ground abstractions and give the reader a checkpoint.

### Characteristic Scales

When introducing a physical quantity, state its characteristic numerical scale. How big is a Schwarzschild radius for a stellar-mass black hole? What's a typical photon impact parameter? What order of magnitude is the Kretschner scalar at the ISCO? Numbers build physical intuition.

---

## 4. Analogies and Intuition

Analogies are primary teaching tools, not decoration. They carry load.

### Structure of a Good Analogy

Every analogy states three things:
1. **The map:** what corresponds to what.
2. **The payoff:** what insight the analogy delivers that pure formalism doesn't.
3. **Where it breaks down:** every analogy fails somewhere, and naming the failure prevents misconceptions.

**Good:** "The Hamiltonian constraint $\mathcal{H} = 0$ acts like a fuel gauge that should always read zero. If the numerical integrator introduces error, the gauge drifts — we monitor it and know exactly how much to distrust the trajectory. The analogy breaks down for timelike geodesics, where $\mathcal{H} = -\tfrac{1}{2}$ rather than zero, but the monitoring principle is identical."

**Bad:** "Think of the Hamiltonian as being like a bank balance."

### Preference Order

1. Physical and geometric analogies (geodesics as "straightest possible paths on a curved surface")
2. Computational analogies (constraint monitoring as "checksums for physics")
3. Everyday analogies (only when they genuinely illuminate — most don't)

### Reuse Across Chapters

When an analogy introduced in an early chapter applies later, reference it by name rather than inventing a new one. This builds a coherent mental model. Track analogies in `continuity.md` to avoid repetition and enable callbacks.

---

## 5. Figures and Experiments

Figures are argument, not illustration. Every figure should change what the reader believes or understands.

### Figure Types

1. **Event-horizon renders** — black hole images, accretion disks, spacetime distortions generated by the event-horizon codebase (Haskell/Rust/WGSL). These connect the physics to the visual output that motivates the book.

2. **Data plots** — convergence curves, error comparisons, spectral coefficients, orbit trajectories. Generated with matplotlib using the pgf backend via `figures/ehplot.py` (which loads `figures/ehbook.mplstyle`).

### Plotting Conventions

- **Colour palette** (Accretion Disk): gold `#C48E36`, blue `#406699`, crimson `#9E302C`, gray `#6E6C76`. Use these consistently — gold for primary data, blue for secondary/reference, crimson for errors or warnings, gray for backgrounds or baselines.
- **Backend:** matplotlib with pgf, producing `.pgf` files that integrate natively with LuaLaTeX. Fonts are set via fontspec in the pgf preamble to match `ehbook.cls` (STIX Two Text, STIX Two Math, Source Code Pro).
- **Experiment scripts** live in the event-horizon repo under `book/`, not in this repo.

### Captions

Substantial: 3–5 sentences, self-contained. A reader skimming the figures should learn something from the captions alone. Include: what is shown, what to notice, what the key quantitative result is.

### Figure Placeholders (for AI Drafting)

During drafting, insert figure placeholders as structured comments:

```latex
% FIGURE PLACEHOLDER
% Description: [What the figure shows]
% Source: [render | data plot | tikz diagram]
% Parameters: [Key parameters for reproduction, e.g., "Schwarzschild, M=10 Msun, observer at r=50M"]
% Caption draft: [3-5 sentence caption]
% Label: fig:...
```

### Numerical Experiments (MacKay's "Small Experiments")

Where appropriate, include small numerical experiments that demonstrate convergence, accuracy, or surprising behaviour. These follow the IFI cycle: motivate the experiment, show the result, interpret what it tells us. Reference the experiment script by its future path in the event-horizon repo.

---

## 6. Code Connection

The event-horizon codebase is a first-class citizen of this book, not an afterthought. Every concept that has a codebase implementation gets a margin reference.

### `\coderef{Module}{Symbol}`

Place at first encounter of a concept implemented in the codebase. The module path uses dot notation (e.g., `Geodesic.Hamiltonian`); the symbol is a type or function name (e.g., `hamiltonianRHS`).

Module paths map to source files:
- Haskell: `Geodesic.Hamiltonian` → `src/EventHorizon/Geodesic/Hamiltonian.hs`
- Rust: `crate_name` → `rust/{crate_name}/src/`
- WGSL: `crate_name` → `rust/{crate_name}/src/*.wgsl`

### Code Excerpts

Short excerpts (5–15 lines) when the code illuminates better than prose. Use `lstlisting` with the appropriate language (`Haskell` or `Rust`). Always show the type signature — in a Haskell codebase, types *are* documentation. Trim module headers and imports.

### Connection Style

Don't merely cite the code — explain how the mathematical structure appears in it. "The function `hamiltonianRHS` takes a polymorphic metric function and the inverse metric as inputs, returning the pair $(\dot{x}^\mu, \dot{p}_\mu)$. The polymorphism in the metric function is what enables automatic differentiation — the same metric code works with both `Double` and `AD` types."

### Margin Note Types

Five types, each with a distinct accent colour (defined in `ehbook.cls`):

| Note | Command | Colour | Use |
|------|---------|--------|-----|
| Physics insight | `\physnote{}` | Blue | Physical interpretation of a result |
| Implementation | `\implnote{}` | Gold | How the codebase implements something |
| Historical | `\histnote{}` | Crimson | Who discovered this, when, context |
| Cross-reference | `\xrefnote{}` | Gray | "See also §X.Y" |
| Warning | `\warnnote{}` | Crimson (bold) | Common pitfall or subtle point |

---

## 7. LaTeX Conventions

### Label Scheme

- Chapters: `ch:name` (e.g., `ch:geodesics`)
- Sections: `sec:name` (e.g., `sec:geo-null`)
- Figures: `fig:name` (e.g., `fig:photon-orbit`)
- Equations: `eq:name` (e.g., `eq:geodesic-hamiltonian`)
- Theorems/definitions: `thm:name` or `def:name`

### Cross-References

Always use `\cref{}` (from cleveref, loaded by `ehbook.cls`). This automatically generates "Section 3.2", "Figure 4.1", etc., and handles capitalisation. Never write "Section~\ref{sec:foo}" — write `\cref{sec:foo}`.

### Citations

Cite liberally. Use the numeric-comp style configured in `ehbook.cls`. Prefer citing at the point of use rather than collecting citations at paragraph end. If a citation key isn't in `references.bib`, flag it as `\cite{TODO:AuthorYear}` for later resolution.

### Section Structure

Use `\section{}` and `\paragraph{}` for within-section structure. Do not use `\subsubsection{}` — the margin is too narrow for deeply nested headings, and it creates visual clutter. If you need finer structure than `\subsection{}`, use `\paragraph{}`.

### Key References

End each chapter with a `\paragraph{Key References.}` block listing the primary sources, briefly annotated.

### Environments

Available theorem-like environments (from `ehbook.cls`):
- `theorem` (blue frame)
- `lemma` (blue frame)
- `proposition` (blue frame)
- `definition` (gold frame)

Use `\chapterepigraph{quote}{attribution}` for chapter-opening quotes.

---

## 8. Anti-Patterns

Explicit list of what to avoid. Each entry shows the bad pattern and a fix.

### "It is well known that..."

If it were well known, the reader wouldn't need this book. State the fact directly.

- Bad: "It is well known that the Kerr metric admits two Killing vectors."
- Good: "The Kerr metric admits two Killing vectors: $\partial_t$ (stationarity) and $\partial_\phi$ (axisymmetry)."

### "It can easily be shown that..."

If it's easy, show it. If it's not easy, don't lie about it.

- Bad: "It can easily be shown that the connection coefficients vanish in normal coordinates."
- Good: "In normal coordinates at a point $p$, the connection coefficients vanish by construction — this is precisely what 'normal' means."

### "Obviously..."

Nothing is obvious. If the reader thought it was obvious, they'd already know it.

- Bad: "Obviously, $\mathcal{H}$ is conserved along the flow."
- Good: "Since $\mathcal{H}$ has no explicit dependence on the affine parameter, Hamilton's equations guarantee that it is conserved along the flow."

### Walls of Equations

More than three consecutive displayed equations without prose. The reader loses the thread. Insert interpretation between derivation steps.

### Orphan Sections

A section with only one or two sentences before the first subsection. If the section has subsections, the section itself needs a substantive introduction (2–3 paragraphs minimum).

### Section-Heading Echo

Repeating the section heading in the first sentence.

- Bad: Section title "Null Geodesics". First sentence: "Null geodesics are geodesics with..."
- Good: Section title "Null Geodesics". First sentence: "Light rays follow the same extremal principle as massive particles, but with the constraint $\mathcal{H} = 0$ enforced along the entire trajectory."

### "In this section we will..."

Throat-clearing. Start with substance, not a table of contents.

- Bad: "In this section we will derive the equations of motion for null geodesics."
- Good: "A photon's trajectory through curved spacetime is entirely determined by the metric and the initial conditions — no mass, no charge, just geometry."

### Hedging Without Substance

"It might be the case that...", "One could argue that...", "It is perhaps worth noting...". Either state it or don't.

---

## 9. Exemplar Passages

Three calibration samples in the target voice. These are benchmarks for tonal consistency.

### 9a. Motivating a Concept (IFI Phase 1)

> A ray tracer needs to answer one question millions of times: given a photon leaving the camera pixel at coordinates $(x, y)$ with momentum $p_\mu$, where does it end up? The photon might spiral into the black hole, escape to the celestial sphere, or — in the most visually interesting case — orbit close to the photon sphere before eventually escaping, carrying the heavily lensed image of the accretion disc.
>
> The Lagrangian formulation gives us the geodesic equation as a second-order ODE, which works but has a practical deficiency: the null constraint $g_{\mu\nu}\dot{x}^\mu \dot{x}^\nu = 0$ isn't enforced by the equations of motion. Numerical error accumulates, and the photon gradually becomes massive. The Hamiltonian formulation avoids this entirely.
> \coderef{Geodesic.Hamiltonian}{hamiltonianRHS}

### 9b. Interpreting a Derivation Result (IFI Phase 3)

> \Cref{eq:geodesic-hamiltonian} reveals something valuable for numerical work: the constraint $\mathcal{H} = 0$ is a first integral of the system. Hamilton's equations preserve it exactly, so any drift in $\mathcal{H}$ during integration is entirely due to numerical error.
> \physnote{The Hamiltonian constraint acts as a built-in accuracy diagnostic — no extra computation required.}
> The codebase monitors $\abs{\mathcal{H}}$ at every integration step. For a well-tuned integrator with adaptive step control, this value remains below $10^{-12}$ throughout a typical ray trace. When it doesn't, the integrator is struggling — usually because the ray is passing dangerously close to the photon sphere, where the effective potential has a saddle point and trajectories are exponentially sensitive to perturbations.

### 9c. Code Connection

> The function `hamiltonianRHS` in \codemodule{Geodesic.Hamiltonian} implements \cref{eq:hamilton-eqs} directly. Its type signature is worth examining:
> \begin{lstlisting}[language=Haskell]
> hamiltonianRHS
>   :: (forall a. Floating a => [a] -> [a])
>   -> Sym4 'Contravariant
>   -> HamiltonianState
>   -> (Vec4 'Contravariant, Vec4 'Covariant)
> \end{lstlisting}
> \implnote{The rank-2 polymorphism in the metric function enables automatic differentiation.}
> The first argument is a *polymorphic* metric function — it works with any `Floating` type, not just `Double`. This is the key to the automatic differentiation strategy developed in \cref{ch:automatic-differentiation}: by passing the same metric function an AD type instead of a `Double`, the code computes exact metric derivatives without finite differences or hand-coded Christoffel symbols. The inverse metric (second argument) is precomputed and passed in, since inverting a $4 \times 4$ matrix is cheap but wasteful to repeat.
