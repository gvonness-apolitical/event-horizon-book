# Continuity Tracker

Updated manually after each `/draft-section` invocation using the continuity notes in the skill output.

---

## Notation Registry

| Symbol | Section Introduced | Meaning |
|--------|--------------------|---------|
| $x^\mu = (t, x, y, z)$ | `sec:sr-minkowski` | Event coordinates; $\mu = 0,1,2,3$ |
| $\eta_{\mu\nu} = \operatorname{diag}(-1,+1,+1,+1)$ | `sec:sr-minkowski` | Minkowski metric (no macro; `\metric` reserved for curved $g_{\mu\nu}$) |
| $\eta^{\mu\nu}$ | `sec:sr-minkowski` | Inverse Minkowski metric (same components in Cartesian coords) |
| $\d s^2$ | `sec:sr-minkowski` | Spacetime interval |
| $V^\mu$ / $V_\mu$ | `sec:sr-minkowski` | Contravariant / covariant components of a four-vector |
| $\Delta\tau = \sqrt{-\Delta s^2}$ | `sec:sr-minkowski` | Proper time for timelike displacements |
| $\Lambda^\mu{}_\nu$ | `sec:sr-lorentz` | Lorentz transformation matrix (bare symbol; `\lorentz` = $W$ is GRMHD Lorentz factor) |
| $\gamma = 1/\sqrt{1-v^2}$ | `sec:sr-lorentz` | SR Lorentz factor (bare $\gamma$; distinct from `\lorentz` = $W$ used in GRMHD chapters) |
| $\phi$ | `sec:sr-lorentz` | Rapidity; $v = \tanh\phi$, $\gamma = \cosh\phi$ |
| $e^\mu{}_{(a)}$ | `sec:sr-lorentz` | Orthonormal tetrad vector (spacetime index up, frame index down in parentheses) |
| $e^{(a)}{}_\mu$ | `sec:sr-lorentz` | Inverse tetrad (mentioned, not yet used) |
| $(a), (b)$ | `sec:sr-lorentz` | Frame indices; raised/lowered with $\eta_{ab}$, not $g_{\mu\nu}$ |
| $O(1,3)$ / $SO^+(1,3)$ | `sec:sr-lorentz` | Lorentz group / proper orthochronous subgroup |
| $k^\mu$ | `sec:sr-causal` | Null four-vector / photon direction |
| $\mathbf{k}$ | `sec:sr-causal` | Spatial part of $k^\mu$ (3-vector, bold); $\abs{\mathbf{k}}^2 = (k^1)^2 + (k^2)^2 + (k^3)^2$ |
| $E$ | `sec:sr-causal` | Photon energy; $k^0 = E$ for future-directed null vector |
| $(\theta, \varphi)$ | `sec:sr-causal` | Spherical angles on observer's celestial sphere $S^2$ |
| $I^+(p)$ / $I^-(p)$ | `sec:sr-causal` | Chronological future / past of event $p$ (timelike curves) |
| $J^+(p)$ / $J^-(p)$ | `sec:sr-causal` | Causal future / past of event $p$ (timelike + null curves) |
| $p_\mu$ | `sec:sr-causal` | Photon four-momentum (covector); $p_0 = -E$ in $(-,+,+,+)$ |
| $\mathbf{p}$ | `sec:sr-causal` | Spatial part of $p_\mu$ (3-vector, bold) |
| eq:null-tetrad | `sec:sr-causal` | Key formula: $k^\mu = E(e^\mu{}_{(0)} + n^i e^\mu{}_{(i)})$ maps pixel $(\theta,\varphi)$ to null vector via tetrad |

## Analogy Registry

| Analogy | Section Used | Maps / Breaks Down |
|---------|--------------|--------------------|
| Translation dictionary (metric) | `sec:sr-minkowski` | Metric converts between vectors and covectors. Breaks: not a literal dictionary; the isomorphism is canonical, not a choice. |
| Ruler-and-clock kit (tetrad) | `sec:sr-lorentz` | Tetrad = observer's local measurement frame. Breaks: tetrads are basis vectors, not physical instruments. |
| Hyperbolic analogue of orthogonality ($\Lambda^T \eta \Lambda = \eta$ vs $R^T R = I$) | `sec:sr-lorentz` | Lorentz condition generalises Euclidean orthogonality. Breaks: $\eta$ is indefinite, so "orthogonality" is in a generalised sense. |
| Hyperbolic analogue of rotation angle (rapidity) | `sec:sr-lorentz` | Rapidities add like rotation angles. Breaks: boosts are non-compact (rapidity unbounded), unlike rotations. |
| Backward ray tracing (CG analogy) | `sec:sr-causal` | Relativistic ray tracing = standard CG backward tracing with null geodesics replacing straight lines. Breaks: CG rays are Euclidean; GR rays curve through spacetime. |
| Celestial sphere / observer's sky | `sec:sr-causal` | Null directions $\leftrightarrow$ points on $S^2$ $\leftrightarrow$ pixels in rendered image. Breaks: spherical parametrisation has coordinate singularities at poles. |

## Forward / Backward References

| Promise | Where Made | Where Fulfilled |
|---------|------------|-----------------|
| Tetrad reappears in camera model | `sec:sr-lorentz` | `ch:camera-rendering` (TBD) |
| Pixel-to-photon-momentum mapping via tetrad | `sec:sr-lorentz` | `ch:camera-rendering` (TBD) |
| $\eta_{\mu\nu} \to g_{\mu\nu}$; index operations identical | `sec:sr-minkowski` | `ch:differential-geometry` (TBD) |
| Null-vector parametrisation reappears in camera model | ch01 intro | `ch:camera-rendering` (TBD) |
| Penrose conformal diagrams needed for black hole causal structure | `sec:sr-causal` | `ch:schwarzschild` (TBD) |
| Geodesic equation governs $k^\mu$ evolution in curved spacetime | `sec:sr-causal` | `ch:differential-geometry` (TBD) |
| eq:null-tetrad is the camera's pixel-to-ray formula | `sec:sr-causal` | `ch:camera-rendering` (TBD) |

## Key Decisions

| Decision | Rationale | Section |
|----------|-----------|---------|
| Signature $(-,+,+,+)$ following MTW | Consistent with codebase (`sym4Diag (-1) 1 1 1`) | `sec:sr-minkowski` |
| Bare $\gamma$ for SR Lorentz factor | `\lorentz` = $W$ is reserved for GRMHD Lorentz factor; different physical quantity | `sec:sr-lorentz` |
| Tetrad via inverse boost | $e^\mu{}_{(a)}$ obtained by applying $\Lambda^\mu{}_\nu\vert_{v \to -v}$ to rest tetrad; transforms $S'$ basis into $S$ coordinates | `sec:sr-lorentz` |
| $e^\mu{}_{(0)} = u^\mu$ stated explicitly | Connects tetrad formalism to four-velocity notation | `sec:sr-lorentz` |
| No macro for $\Lambda^\mu{}_\nu$ | Single Greek letter, used only in SR chapters; `\lorentz` already taken | `sec:sr-lorentz` |
| Covector $p_\mu$ as ray tracer variable | Hamiltonian formulation uses covariant components; Killing symmetries yield conserved $p_\mu \xi^\mu$ directly | `sec:sr-causal` |
| $E = 1$ for null rays | Affine parametrisation freedom; trajectory independent of energy | `sec:sr-causal` |
| Past light cone for backward ray tracing | Standard CG practice; trace from camera to sources, not sources to camera | `sec:sr-causal` |
