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
| $\mathcal{M}$ | `sec:dg-manifolds` | Smooth manifold (topological space, Hausdorff, second-countable, locally $\mathbb{R}^n$) |
| $(U, \varphi)$ | `sec:dg-manifolds` | Coordinate chart; $\varphi : U \to \mathbb{R}^n$. Note: $\varphi$ reuses glyph from celestial-sphere angle in `sec:sr-causal`; context distinguishes |
| $\psi \circ \varphi^{-1}$ | `sec:dg-manifolds` | Transition map between overlapping charts |
| $T_p\mathcal{M}$ | `sec:dg-manifolds` | Tangent space at $p$; vector space of directional derivative operators (derivations on germs) |
| $T^*_p\mathcal{M}$ | `sec:dg-manifolds` | Cotangent space at $p$; dual of $T_p\mathcal{M}$; elements are one-forms/covectors |
| $\mathbf{e}_{(\mu)} = \pd{\mu}$ | `sec:dg-manifolds` | Coordinate basis vectors for $T_p\mathcal{M}$ |
| $\d x^\mu$ | `sec:dg-manifolds` | Coordinate basis one-forms for $T^*_p\mathcal{M}$; dual to $\pd{\mu}$ |
| $\delta^\mu{}_\nu$ | `sec:dg-manifolds` | Kronecker delta; $\d x^\mu(\pd{\nu}) = \delta^\mu{}_\nu$ |
| $\partial x'^\mu / \partial x^\nu$ | `sec:dg-manifolds` | Jacobian matrix of coordinate transformation; pushforward of transition map |
| $\metric$ (`\metric`) | `sec:dg-metric` | Curved-spacetime metric tensor; symmetric, non-degenerate $(0,2)$ tensor |
| $\inversemetric$ (`\inversemetric`) | `sec:dg-metric` | Inverse metric tensor; symmetric $(2,0)$ tensor; $g^{\mu\alpha}g_{\alpha\nu} = \delta^\mu{}_\nu$ |
| $g = \det(\metric)$ | `sec:dg-metric` | Metric determinant; non-zero by non-degeneracy |
| $\d s^2 = \metric\,\d x^\mu\,\d x^\nu$ | `sec:dg-metric` | Line element; generalises flat-spacetime interval to curved manifolds |
| $\flat$ / $\sharp$ | `sec:dg-metric` | Musical isomorphism: $\flat$ = index lowering, $\sharp$ = index raising |
| $\cd{\mu}$ (`\cd`) | `sec:dg-covariant` | Covariant derivative (Levi-Civita connection); $\cd{\mu} f = \pd{\mu} f$ on scalars |
| $\christoffel{\lambda}{\mu}{\nu}$ (`\christoffel`) | `sec:dg-covariant` | Christoffel symbols of the second kind; $= \frac{1}{2} g^{\lambda\sigma}(\pd{\mu} g_{\nu\sigma} + \pd{\nu} g_{\mu\sigma} - \pd{\sigma} g_{\mu\nu})$ |
| $\lambda$ | `sec:dg-geodesic` | Affine parameter along a geodesic; $\lambda = \tau$ (proper time) for timelike geodesics |
| $\dot{x}^\mu$, $\ddot{x}^\mu$ | `sec:dg-geodesic` | Overdot = $\d / \d\lambda$; tangent vector and acceleration along a curve |
| $L = \tfrac{1}{2}\metric\,\dot{x}^\mu\,\dot{x}^\nu$ | `sec:dg-geodesic` | Geodesic Lagrangian; $2L$ = squared norm of tangent vector |
| $p_\mu = \metric\,\dot{x}^\nu$ | `sec:dg-geodesic` | Conjugate momentum (index-lowered tangent vector); extends $p_\mu$ from `sec:sr-causal` to curved spacetime |
| $\mathcal{H} = \tfrac{1}{2}\inversemetric\,p_\mu\,p_\nu$ | `sec:dg-geodesic` | Geodesic super-Hamiltonian; $\mathcal{H} = 0$ for null, $-\tfrac{1}{2}$ for timelike |
| $\riemann{\rho}{\sigma}{\mu}{\nu}$ (`\riemann`) | `sec:dg-curvature` | Riemann curvature tensor; $(1,3)$ tensor defined via $[\cd{\mu}, \cd{\nu}]V^\rho = \riemann{\rho}{\sigma}{\mu}{\nu} V^\sigma$ |
| $R_{\rho\sigma\mu\nu}$ | `sec:dg-curvature` | Fully covariant Riemann tensor; $= g_{\rho\alpha}\riemann{\alpha}{\sigma}{\mu}{\nu}$; 20 independent components in 4D |
| $\ricci$ (`\ricci`) | `sec:dg-curvature` | Ricci tensor; $= \riemann{\lambda}{\mu}{\lambda}{\nu}$; 10 independent components; symmetric |
| $\ricciscalar$ (`\ricciscalar`) | `sec:dg-curvature` | Ricci scalar; $= \inversemetric R_{\mu\nu}$; note: glyph collides with sphere radius $R$ in $S^2$ examples |
| $\einstein$ (`\einstein`) | `sec:dg-curvature` | Einstein tensor; $= \ricci - \tfrac{1}{2}\metric\ricciscalar$; divergence-free by contracted Bianchi identity |
| $\weyl{\rho}{\sigma}{\mu}{\nu}$ (`\weyl`) | `sec:dg-curvature` | Weyl tensor; trace-free part of Riemann; 10 independent components in 4D; vanishes for $n \leq 3$ |
| $\stressenergy$ (`\stressenergy`) | `sec:dg-curvature` | Stress-energy tensor; first appearance in Einstein equation $\einstein = 8\pi\stressenergy$ |
| $K = \ricciscalar/2$ | `sec:dg-curvature` | Gaussian curvature (2D); $= 1/R^2$ for sphere of radius $R$ |
| $\Phi$ | `sec:gr-efe` | Newtonian gravitational potential; $\laplacian\Phi = 4\pi\rho$ |
| $T = \inversemetric\,\stressenergy$ | `sec:gr-efe` | Trace of stress-energy tensor |
| $\Lambda$ | `sec:gr-efe` | Cosmological constant; set to $0$ for the remainder of the book |
| $S = \int\ricciscalar\,\detmetric\,\vol{4}$ | `sec:gr-efe` | Einstein--Hilbert action (histnote only; not a recurring symbol) |
| $\rho$ | `sec:gr-stress-energy` | Total energy density (rest-mass + internal energy); distinct from $\restmassdensity$ (rest-mass density in GRMHD) |
| $p$ | `sec:gr-stress-energy` | Isotropic pressure in perfect-fluid stress-energy tensor |
| $u^\mu$ | `sec:gr-stress-energy` | Fluid four-velocity; normalised $\metric u^\mu u^\nu = -1$ |
| $F_{\mu\nu}$ | `sec:gr-stress-energy` | Faraday tensor; antisymmetric $(0,2)$ tensor encoding $E$ and $B$ fields |
| $T^{\mu\nu}_{\text{EM}}$ | `sec:gr-stress-energy` | Electromagnetic stress-energy tensor; trace-free |
| $v^\mu$ | `sec:gr-stress-energy` | Generic future-directed timelike vector (used in energy condition statements) |
| $b_0$ | `sec:gr-stress-energy` | Morris--Thorne wormhole throat radius |
| $h_{\mu\nu}$ | `sec:gr-weak-field` | Metric perturbation; $\metric = \eta_{\mu\nu} + h_{\mu\nu}$, $\abs{h_{\mu\nu}} \ll 1$ |
| $h^{\mu\nu} \equiv \eta^{\mu\alpha}\eta^{\nu\beta}h_{\alpha\beta}$ | `sec:gr-weak-field` | Perturbation with indices raised by background metric |
| $\xi^\mu$ | `sec:gr-weak-field` | Killing vector; $\xi^\mu = (1,\mathbf{0})$ for static spacetimes |
| $E = -p_\mu\,\xi^\mu = -p_0$ | `sec:gr-weak-field` | Killing energy; $> 0$ for future-directed photons; conserved along geodesics |
| $z$ | `sec:gr-weak-field` | Gravitational redshift parameter; $1 + z = \nu_{\text{em}}/\nu_{\text{rec}}$ |
| $\nu$ | `sec:gr-weak-field` | Photon frequency measured by a static observer; $\nu \propto 1/\sqrt{-g_{00}}$ |
| $M$ | `sec:gr-weak-field` | Black hole mass in geometric units ($G = c = 1$); $M_\odot \approx 1.5\;\text{km}$ |
| $f$ | `sec:gr-exact-solutions` | Kerr--Schild scalar function; $\metric = \eta_{\mu\nu} + f\,l_\mu\,l_\nu$ |
| $l_\mu$ | `sec:gr-exact-solutions` | Kerr--Schild null covector; null w.r.t.\ both $\eta_{\mu\nu}$ and $\metric$ |
| $a = J/M$ | `sec:gr-exact-solutions` | Kerr spin parameter (specific angular momentum); $\abs{a} \leq M$ for black holes |
| $\Sigma = r^2 + a^2\cos^2\theta$ | `sec:gr-exact-solutions` | Kerr oblate-spheroid factor; encodes $\theta$-dependence from rotation |
| $\Delta = r^2 - 2Mr + a^2$ | `sec:gr-exact-solutions` | Kerr horizon function; roots $r_\pm = M \pm \sqrt{M^2 - a^2}$ are event horizons |
| $r_+$, $r_-$ | `sec:gr-exact-solutions` | Outer (event) and inner (Cauchy) horizons of Kerr; $r_\pm = M \pm \sqrt{M^2 - a^2}$ |
| $\ell$ | `sec:gr-exact-solutions` | Proper radial distance from Morris--Thorne throat; $\ell = 0$ at throat |
| $\Phi(\ell)$ | `sec:gr-exact-solutions` | Morris--Thorne redshift function; set to $0$ in the codebase (zero-tidal-force case) |
| $\alpha(t,r)$, $\beta(t,r)$ | `sec:schw-derivation` | Metric functions in spherically symmetric ansatz; local to derivation, not reused |
| $C$ | `sec:schw-derivation` | Integration constant identified as $2M$ via weak-field limit; local to derivation |
| $r_*$ | `sec:schw-coordinates` | Tortoise coordinate; $r_* = r + 2M\ln(r/2M - 1)$ for $r > 2M$; defined by \cref{eq:tortoise} |
| $v = t + r_*$ | `sec:schw-coordinates` | Advanced time (ingoing EF null coordinate); $v = \text{const}$ labels ingoing null rays. Note: $v$ collides with velocity if used elsewhere; context distinguishes |
| $u = t - r_*$ | `sec:schw-coordinates` | Retarded time (outgoing EF null coordinate); $u = \text{const}$ labels outgoing null rays |
| $\psi^\mu = \partial_\varphi$ | `sec:schw-orbits` | Rotational Killing vector (axisymmetry); conserved $L = p_\mu \psi^\mu$ |
| $L$ (angular momentum) | `sec:schw-orbits` | Specific angular momentum; $L = p_\varphi = r^2\dot{\varphi}$ in equatorial plane. Note: $L$ reused from geodesic Lagrangian in `sec:dg-geodesic`; context distinguishes (Lagrangian does not appear in `sec:schw-orbits`) |
| $\kappa$ | `sec:schw-orbits` | Geodesic norm indicator: $\kappa = -1$ (timelike), $\kappa = 0$ (null); $\metric\dot{x}^\mu\dot{x}^\nu = \kappa$ |
| $V_{\text{eff}}(r)$ | `sec:schw-orbits` | Effective potential for radial geodesic motion; $\dot{r}^2 = E^2 - V_{\text{eff}}$ |
| $b = L/E$ | `sec:schw-orbits` | Impact parameter for null geodesics |
| $b_c = 3\sqrt{3}\,M$ | `sec:schw-orbits` | Critical impact parameter; photons with $b < b_c$ captured, $b > b_c$ deflected |
| $r_{\text{ISCO}} = 6M$ | `sec:schw-orbits` | Innermost stable circular orbit radius (Schwarzschild); inner edge of thin accretion disc |
| $\eta = 1 - 2\sqrt{2}/3 \approx 5.7\%$ | `sec:schw-orbits` | Radiative efficiency for accretion onto Schwarzschild black hole |
| $\bar{t} = v - r$ | `sec:schw-kerr-schild` | Kerr-Schild time coordinate; differs from Schwarzschild $t$ by $2M\ln(r/2M-1)$ for $r > 2M$ |
| $n^i = x^i/r$ | `sec:schw-kerr-schild` | Euclidean unit radial vector ($i = 1,2,3$); $n_i = n^i$ in Cartesian coordinates |

## Analogy Registry

| Analogy | Section Used | Maps / Breaks Down |
|---------|--------------|--------------------|
| Translation dictionary (metric) | `sec:sr-minkowski` | Metric converts between vectors and covectors. Breaks: not a literal dictionary; the isomorphism is canonical, not a choice. |
| Ruler-and-clock kit (tetrad) | `sec:sr-lorentz` | Tetrad = observer's local measurement frame. Breaks: tetrads are basis vectors, not physical instruments. |
| Hyperbolic analogue of orthogonality ($\Lambda^T \eta \Lambda = \eta$ vs $R^T R = I$) | `sec:sr-lorentz` | Lorentz condition generalises Euclidean orthogonality. Breaks: $\eta$ is indefinite, so "orthogonality" is in a generalised sense. |
| Hyperbolic analogue of rotation angle (rapidity) | `sec:sr-lorentz` | Rapidities add like rotation angles. Breaks: boosts are non-compact (rapidity unbounded), unlike rotations. |
| Backward ray tracing (CG analogy) | `sec:sr-causal` | Relativistic ray tracing = standard CG backward tracing with null geodesics replacing straight lines. Breaks: CG rays are Euclidean; GR rays curve through spacetime. |
| Celestial sphere / observer's sky | `sec:sr-causal` | Null directions $\leftrightarrow$ points on $S^2$ $\leftrightarrow$ pixels in rendered image. Breaks: spherical parametrisation has coordinate singularities at poles. |
| Arrows vs. directional derivatives | `sec:dg-manifolds` | Euclidean vectors as arrows $\to$ tangent vectors as derivative operators. Maps: both have magnitude and direction; derivatives capture "rate of change along a direction". Breaks: derivative operators don't have visual geometric intuition; the "arrow" picture fails on curved manifolds without ambient space. |
| Curved-spacetime dot product (metric) | `sec:dg-metric` | Metric generalises the Euclidean/Minkowski dot product to curved manifolds. Maps: assigns size to displacements and angles between directions. Breaks: Lorentzian signature makes the "dot product" indefinite, so "length" can be negative. |
| Straightest path (geodesic as autoparallel) | `sec:dg-geodesic` | Flat-spacetime straight lines $\to$ geodesics on curved manifolds. Maps: both are paths with zero acceleration relative to the geometry. Breaks: on curved manifolds multiple geodesics can connect the same two points. |
| Parallel-transport loop / vector rotation | `sec:dg-curvature` | Vector parallel-transported around closed loop on sphere returns rotated; rotation angle = enclosed curvature. Maps: flat space → no rotation; curved → nonzero rotation. Breaks: only exact for small loops (infinitesimal limit gives Riemann tensor). |
| Geometry-matter divergence-free pairing | `sec:gr-efe` | Einstein tensor (geometry) and stress-energy tensor (matter) are both symmetric, divergence-free $(0,2)$ tensors; EFE equates them. Maps: divergence-free ↔ conservation law. Breaks: the pairing is a postulate, not a theorem; other divergence-free tensors exist ($\Lambda g_{\mu\nu}$). |
| Pressure gravitates (inertia analogy) | `sec:gr-stress-energy` | Combination $\rho + p$ rather than $\rho$ alone enters perfect-fluid stress-energy because pressure contributes to inertia. Maps: explains TOV limit. Breaks: "pressure gravitates" is a loose statement; the full tensor structure matters. |
| Trace as radiation barometer | `sec:gr-stress-energy` | $T = -\rho + 3p$ measures the balance between energy density and pressure; vanishes for radiation ($\rho = 3p$). Maps: connects equation of state to trace of field equations. Breaks: real matter has mixed composition; trace zero does not imply pure radiation. |
| Metric encodes gravitational potential | `sec:gr-weak-field` | $g_{00} = -(1 + 2\Phi)$ bridges GR and Newtonian gravity; the time--time metric component is the gravitational potential. Maps: Newton's $\laplacian\Phi = 4\pi\rho$ $\leftrightarrow$ Einstein equations. Breaks: only valid for weak, static fields. |
| Photons climbing out of potential wells | `sec:gr-weak-field` | Photon frequency decreases as it escapes a gravitational well (like a ball losing kinetic energy climbing a hill). Maps: energy conservation / redshift. Breaks: photons do not slow down; they lose energy by decreasing frequency, not speed. |
| City-scale distances for Schwarzschild radii | `sec:gr-exact-solutions` | Event horizon ($30\;\text{km}$), photon sphere ($44\;\text{km}$), ISCO ($89\;\text{km}$) for $10\,M_\odot$ black hole. Maps: gives visceral sense of compactness. Breaks: comparison to city geography is purely for scale; spacetime geometry near a black hole is nothing like a city. |
| Newton's shell theorem (gravitational analogue) | `sec:schw-derivation` | Birkhoff's theorem = GR shell theorem: spherically symmetric vacuum exterior is static and unique regardless of interior dynamics. Maps: spherical symmetry → external field depends only on total mass. Breaks: GR version also forces staticity, which has no Newtonian analogue. |
| One-way membrane (event horizon) | `sec:schw-coordinates` | Light cones tilt inward at $r = 2M$; all future-directed null rays have $\d r < 0$ inside. Maps: door that opens only inward. Breaks: nothing locally special happens at the membrane; it is a global causal property. |
| Newtonian effective potential (structural analogy) | `sec:schw-orbits` | GR $V_{\text{eff}}$ = Newtonian terms + $-2ML^2/r^3$ correction. Maps: same gravitational + centrifugal structure; same turning-point analysis. Breaks: GR uses $\dot{r}^2 = E^2 - V$ (not $\frac{1}{2}\dot{r}^2 = E - V$); magnitudes differ by factors of 2. |
| Neumann series truncation (null property) | `sec:schw-kerr-schild` | Generic metric inverse requires infinite Neumann series; null rank-one perturbation truncates after one term. Maps: explains why KS inverse is a simple sign flip. Breaks: only applies to rank-one perturbations with null vector; Kerr case works because the same structure holds. |

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
| Coordinate singularities at horizon discussed later | `sec:dg-manifolds` | `ch:schwarzschild` (TBD) |
| Metric tensor generalises $\eta_{\mu\nu}$ to curved manifolds | `sec:dg-manifolds` | `sec:dg-metric` ✓ |
| Schwarzschild metric preview | `sec:dg-metric` | `ch:schwarzschild` (TBD) |
| Covariant derivative built from metric via Christoffel symbols | `sec:dg-metric` | `sec:dg-covariant` ✓ |
| Inverse metric in geodesic Hamiltonian ($p_\mu \to \dot{x}^\mu$) | `sec:dg-metric` | `ch:geodesics` (TBD) |
| Christoffel symbols and geodesics connection | `sec:dg-covariant` | `sec:dg-geodesic` ✓ |
| Metric compatibility enables Lagrangian/Hamiltonian interchange | `sec:dg-covariant` | `sec:dg-geodesic` ✓ |
| AD strategy for Christoffel computation | `sec:dg-covariant` | `ch:autodiff` (TBD) |
| Geodesic equation is curved-spacetime generalisation of photon trajectory eq | `sec:dg-geodesic` | `sec:sr-causal` (backward ref) |
| Full numerical integration strategy (adaptive step, Killing vectors, termination) | `sec:dg-geodesic` | `ch:geodesics` (TBD) |
| Einstein--Cartan theory (torsion makes autoparallels ≠ extremals) | `sec:dg-geodesic` | Not planned (historical aside) |
| Einstein field equations and their physical content | `sec:dg-curvature` | `sec:gr-efe` ✓ |
| Gravitational lensing / image distortions via Weyl tensor | `sec:dg-curvature` | Ray tracer chapters (TBD) |
| Weak-field limit recovers Newtonian gravity | `sec:gr-efe` | `sec:gr-weak-field` ✓ |
| Vacuum equations as starting point for Schwarzschild/Kerr | `sec:gr-efe` | `ch:schwarzschild`, `ch:kerr` (TBD) |
| ADM initial-value decomposition (constraint vs evolution eqs) | `sec:gr-efe` | `ch:adm-decomposition` (TBD) |
| Stress-energy tensors for perfect fluids and EM fields | `sec:gr-efe` | `sec:gr-stress-energy` ✓ |
| $3{+}1$ decomposition of perfect-fluid conservation → GRMHD | `sec:gr-stress-energy` | Part~V (TBD) |
| $\rho$ vs $\restmassdensity$ distinction used in GRMHD formulation | `sec:gr-stress-energy` | Part~V (TBD) |
| NEC needed for Penrose singularity theorem and area theorem | `sec:gr-stress-energy` | Penrose theorem chapter (TBD) |
| Morris--Thorne wormhole detailed treatment | `sec:gr-stress-energy` | `sec:gr-exact-solutions` ✓ |
| Exact redshift in ray tracer spectral calculations | `sec:gr-weak-field` | Ray tracer chapters (TBD) |
| Schwarzschild metric $g_{00} = -(1-2M/r)$ used in exact redshift | `sec:gr-weak-field` | `sec:gr-exact-solutions` ✓ |
| Gravitational + Doppler shift produces asymmetric brightness pattern | `sec:gr-weak-field` | Ray tracer chapters (TBD) |
| Birkhoff's theorem derivation | `sec:gr-exact-solutions` | `sec:schw-derivation` ✓ |
| Schwarzschild orbits: photon sphere, ISCO | `sec:gr-exact-solutions` | `sec:schw-orbits` ✓ |
| Coordinate singularity resolution | `sec:gr-exact-solutions` | `sec:schw-coordinates` ✓ |
| Kerr ISCO prograde efficiency $\eta \approx 42\%$ | `sec:schw-orbits` | `sec:kerr-isco` (TBD) |
| Kerr--Schild coordinates for Schwarzschild | `sec:gr-exact-solutions` | `sec:schw-kerr-schild` ✓ |
| Kerr Boyer--Lindquist derivation | `sec:gr-exact-solutions` | `ch:kerr` (TBD) |
| AD strategy for Christoffel computation | `sec:gr-exact-solutions` | `ch:autodiff` (TBD) |
| Coordinate singularity resolution at $r=2M$ | `sec:schw-derivation` | `sec:schw-coordinates` ✓ |
| Weak-field identification of $M$ | `sec:schw-derivation` | `sec:gr-weak-field` (backward ref ✓) |
| Kruskal--Szekeres construction and Penrose diagrams | `sec:schw-coordinates` | `sec:schw-kruskal` (TBD) |
| Kerr--Schild coordinates as codebase default | `sec:schw-coordinates` | `sec:schw-kerr-schild` ✓ |
| Kerr--Schild form of Kerr metric | `sec:schw-kerr-schild` | `sec:kerr-ks` (TBD) |

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
| Tangent vectors as derivations on germs | Standard modern approach (Carroll, Wald); avoids equivalence classes of curves | `sec:dg-manifolds` |
| $\varphi$ reused for chart maps | Different context from celestial-sphere $\varphi$ in `sec:sr-causal`; standard notation in differential geometry | `sec:dg-manifolds` |
| Hausdorff + second-countable stated in definition | Mathematical completeness; prevents pathological examples | `sec:dg-manifolds` |
| Metric as `Sym4 'Covariant` | 10 independent components matching mathematical symmetry; phantom variance prevents mixing | `sec:dg-metric` |
| Geometric units $G = c = 1$ in Schwarzschild preview | Standard GR convention; used throughout later chapters | `sec:dg-metric` |
| Two-sphere as worked example (Riemannian) | Familiar curved geometry; demonstrates index operations without Lorentzian complications | `sec:dg-metric` |
| Christoffel4 = four Sym4 'Covariant | One symmetric matrix per upper index; 40 components total | `sec:dg-covariant` |
| AD over hand-coded Christoffel expressions | Polymorphic metric + AD eliminates hand-differentiation; generalises to any metric | `sec:dg-covariant` |
| Cyclic-permutation derivation of Christoffel formula | Standard derivation with all three permuted equations shown explicitly | `sec:dg-covariant` |
| Dual derivation of geodesic equation (parallel transport + variational) | Both derivations shown; equivalence stated as theorem for Levi-Civita connection | `sec:dg-geodesic` |
| Hamiltonian formulation preferred for numerics | First-order ODE system; conserved $\mathcal{H}$ as error diagnostic; conserved $p_\mu$ from Killing symmetries | `sec:dg-geodesic` |
| Covariant momentum equation via Euler--Lagrange | $\dot{p}_\mu = \tfrac{1}{2}(\pd{\mu}g_{\alpha\beta})\dot{x}^\alpha\dot{x}^\beta$ avoids differentiating inverse metric; matches codebase AD strategy | `sec:dg-geodesic` |
| $S^2$ worked example continued from sec:dg-covariant | Geodesic equation verified on equator; non-geodesic latitude circle as contrast | `sec:dg-geodesic` |
| $S^2$ worked example continued to curvature | Riemann, Ricci, scalar curvature computed explicitly; Gaussian curvature $K = 1/R^2$ recovered | `sec:dg-curvature` |
| Sign convention: Carroll/Wald for Riemann tensor | Upper index first, no minus sign in commutator definition; same sign as MTW but different index ordering | `sec:dg-curvature` |
| $R$ / $\ricciscalar$ glyph collision with sphere radius | Acknowledged in `\warnnote`; context resolves; standard in GR literature | `sec:dg-curvature` |
| Weyl decomposition uses compact antisymmetrisation | $g_{\rho[\mu}R_{\nu]\sigma}$ includes $\tfrac{1}{2}$ factor; distinct from expanded form with explicit $\tfrac{1}{2}$ coefficients | `sec:dg-curvature` |
| $\Lambda = 0$ for the entire book | Cosmological constant negligible at black-hole scales ($\Lambda M^2 \sim 10^{-46}$ for solar-mass) | `sec:gr-efe` |
| Lovelock uniqueness for Einstein tensor | $\einstein + \Lambda\metric$ is the unique divergence-free symmetric $(0,2)$ tensor linear in second derivatives of the metric | `sec:gr-efe` |
| Constraint vs evolution equation split: 4+6 | Bianchi identity → 6 independent equations; 4 constraints + 6 evolution in ADM | `sec:gr-efe` |
| $\rho$ = total energy density, not rest-mass density | $\rho_0$ (`\restmassdensity`) reserved for rest-mass density in GRMHD; $\rho$ includes internal energy | `sec:gr-stress-energy` |
| Energy conditions are sufficient conditions, not laws | WEC, NEC, SEC, DEC are useful for theorems but can be violated (Casimir, cosmological constant) | `sec:gr-stress-energy` |
| Kerr--Schild as default coordinate system | Horizon-penetrating; $\metric$ finite at $r = 2M$; inverse metric equally simple ($\eta^{\mu\nu} - f l^\mu l^\nu$); used for both Schwarzschild and Kerr | `sec:gr-exact-solutions` |
| Morris--Thorne zero-redshift form ($\Phi = 0$) | Simplest member of the MT family; codebase implements this case; $g_{tt} = -1$ everywhere | `sec:gr-exact-solutions` |
| $z$ Cartesian coordinate vs $z$ redshift parameter | Standard GR notation; context distinguishes (Cartesian $z$ appears only in Kerr--Schild data; redshift $z$ from `sec:gr-weak-field`); analogous to $\varphi$ chart/celestial-sphere collision | `sec:gr-exact-solutions` |
| Exponential parametrisation for ansatz | $e^{2\alpha}$, $e^{2\beta}$ keeps metric components manifestly positive and simplifies Ricci algebra | `sec:schw-derivation` |
| No `\coderef` in derivation section | Codebase uses Kerr--Schild coordinates, not Schwarzschild coordinates; `\coderef{Spacetime}{Schwarzschild}` placed on `sec:schw-coordinates` instead | `sec:schw-derivation` |
| Cartesian initial conditions in codebase | Codebase sets up initial conditions in Cartesian Kerr--Schild coordinates, not spherical EF coordinates | `sec:schw-coordinates` |
| EF coordinates pedagogical, not computational | Ingoing EF used for geometric intuition (one-way membrane, light cone tilting); Kerr--Schild used for numerics | `sec:schw-coordinates` |
| $L$ reused for angular momentum | Standard GR convention; geodesic Lagrangian $L$ from `sec:dg-geodesic` does not appear in orbits chapter; disambiguation sentence at first use | `sec:schw-orbits` |
| $\dot{r}^2 = E^2 - V_{\text{eff}}$ convention | Follows Carroll/Wald; differs from Newtonian $\frac{1}{2}\dot{r}^2 = E - V$ by factors of 2; noted in warnnote | `sec:schw-orbits` |
| $n_i$ vs $n^i$ in KS components | Covariant metric uses $n_i$, contravariant uses $n^i$; parenthetical notes $n_i = n^i$ in Cartesian coordinates | `sec:schw-kerr-schild` |
| $f = 2M/r$ specialisation of KS scalar | Schwarzschild case of the general Kerr--Schild scalar $f$ introduced in `sec:gr-exact-solutions` | `sec:schw-kerr-schild` |
