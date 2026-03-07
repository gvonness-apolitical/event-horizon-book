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
| $\Sigma$ | `sec:gr-exact-solutions`, re-derived `sec:kerr-bl` | $r^2 + a^2\cos^2\theta$; oblate-spheroid factor; $\Sigma = 0$ at ring singularity |
| $\Delta$ | `sec:gr-exact-solutions`, re-derived `sec:kerr-bl` | $r^2 - 2Mr + a^2$; horizon function; roots $r_\pm$ are horizons |
| $A = (r^2 + a^2)^2 - a^2\Delta\sin^2\theta$ | `sec:kerr-bl` | Azimuthal metric auxiliary; governs circumferential radius |
| eq:kerr-bl-metric | `sec:kerr-bl` | Full Boyer--Lindquist line element for Kerr |
| eq:bl-quartic | `sec:kerr-bl` | BL-to-Cartesian radius relation; $r^4 - (p^2 - a^2)r^2 - a^2z^2 = 0$ |
| $\bar{t}$, $\bar{\varphi}$ (Kerr) | `sec:kerr-ks` | Ingoing Kerr--Schild time and azimuthal coordinates; defined differentially via eq:kerr-ks-transform |
| $f = 2Mr/\Sigma = 2Mr^3/(r^4 + a^2z^2)$ | `sec:gr-exact-solutions`, used `sec:kerr-ks` | Kerr KS scalar function; specialises to $2M/r$ at $a=0$ |
| $l_\mu$ (Kerr KS) | `sec:gr-exact-solutions`, used `sec:kerr-ks` | Kerr ingoing KS null covector; twisted by spin; eq:kerr-ks-null |
| eq:kerr-ks-metric | `sec:kerr-ks` | $\metric = \eta_{\mu\nu} + f\,l_\mu\,l_\nu$ for Kerr |
| eq:kerr-ks-inverse | `sec:kerr-ks` | $\inversemetric = \eta^{\mu\nu} - f\,l^\mu\,l^\nu$ for Kerr |
| eq:kerr-oblate-spheroidal | `sec:kerr-ks` | Oblate spheroidal coordinate relations; $x+iy = (r+ia)e^{i\bar{\varphi}}\sin\theta$ |
| $p^2 \equiv x^2 + y^2 + z^2$ | `sec:kerr-bl-quartic` | Squared Euclidean distance; local to quartic derivation; disambiguated from pressure $p$ (`sec:gr-stress-energy`) and momentum $p_\mu$ (`sec:sr-causal`) |
| $\mathcal{D} = (p^2 - a^2)^2 + 4a^2z^2$ | `sec:kerr-bl-quartic` | Discriminant of BL radius quadratic; non-negative (sum of squares) |
| $u = r^2$ | `sec:kerr-bl-quartic` | Substitution variable for biquadratic reduction; local to derivation |
| eq:bl-quartic-derived | `sec:kerr-bl-quartic` | Re-derivation of eq:bl-quartic from oblate spheroidal relations |
| eq:bl-r-solution | `sec:kerr-bl-quartic` | Closed-form BL radius; $r = \sqrt{u_+}$ with $u_+$ from quadratic formula |
| eq:kerr-horizons | `sec:kerr-horizons` | $r_\pm = M \pm \sqrt{M^2 - a^2}$; event and Cauchy horizon radii |
| eq:kerr-gtt | `sec:kerr-horizons` | $g_{tt} = -(\Delta - a^2\sin^2\theta)/\Sigma$; time--time metric component |
| $r_{\text{ergo}}(\theta)$ | `sec:kerr-horizons` | $M + \sqrt{M^2 - a^2\cos^2\theta}$; outer ergosphere boundary |
| eq:kerr-ergosphere | `sec:kerr-horizons` | Ergosphere radius as function of polar angle |
| $\omega = 2Mar/A$ | `sec:kerr-horizons` | ZAMO angular velocity; frame-dragging rate |
| eq:kerr-omega | `sec:kerr-horizons` | ZAMO angular velocity formula |
| $\omega_H = a/(r_+^2 + a^2)$ | `sec:kerr-horizons` | Horizon angular velocity |
| eq:kerr-omega-horizon | `sec:kerr-horizons` | Horizon angular velocity formula |
| eq:kerr-omega-far | `sec:kerr-horizons` | Far-field frame dragging; $\omega \approx 2Ma/r^3$ |
| $a_* \equiv a/M$ | `sec:kerr-isco` | Dimensionless spin parameter; $\abs{a_*} \leq 1$ for black holes |
| $R(r)$ | `sec:kerr-isco` | Kerr radial quartic polynomial; eq:kerr-radial-R. Note: glyph collides with Ricci scalar $\ricciscalar$; context distinguishes |
| eq:kerr-radial-R | `sec:kerr-isco` | $R(r) = [E(r^2+a^2)-aL]^2 - \Delta[r^2+(L-aE)^2]$; Kerr radial quartic |
| eq:kerr-circ-E | `sec:kerr-isco` | Specific energy for circular Kerr orbit; $\pm$ upper sign = prograde |
| eq:kerr-circ-L | `sec:kerr-isco` | Specific angular momentum for circular Kerr orbit |
| $Z_1$, $Z_2$ | `sec:kerr-isco` | Bardeen--Press--Teukolsky auxiliary functions for ISCO; local to derivation |
| eq:kerr-Z1, eq:kerr-Z2 | `sec:kerr-isco` | Auxiliary function definitions |
| eq:kerr-isco | `sec:kerr-isco` | $r_{\text{ISCO}} = M(3 + Z_2 \mp \sqrt{(3-Z_1)(3+Z_1+2Z_2)})$; $\mp$ upper sign = prograde |
| $\eta = 1 - E_{\text{ISCO}}$ | `sec:kerr-isco` | General Kerr radiative efficiency; extends $\eta \approx 5.7\%$ from `sec:schw-orbits` |
| $\eta_{\text{max}} = 1 - 1/\sqrt{3} \approx 42.3\%$ | `sec:kerr-isco` | Extremal prograde Kerr efficiency |
| eq:kerr-efficiency, eq:kerr-efficiency-max | `sec:kerr-isco` | Radiative efficiency formulae |
| $\rho = \abs{\ell}$ | `sec:kerr-wormhole` | Cartesian radial coordinate for Morris--Thorne; $\rho = \sqrt{x^2+y^2+z^2}$; throat at $\rho = 0$. Note: glyph collides with energy density $\rho$ (`sec:gr-stress-energy`); context distinguishes |
| eq:mt-metric | `sec:kerr-wormhole` | Morris--Thorne line element in $(\ell,\theta,\varphi)$ coordinates; reproduces eq:morris-thorne-metric |
| eq:mt-cartesian-spatial | `sec:kerr-wormhole` | $g_{ij} = (1+b_0^2/\rho^2)\delta_{ij} - (b_0^2/\rho^2)n_in_j$; Cartesian spatial metric |
| eq:mt-cartesian-inverse | `sec:kerr-wormhole` | Inverse spatial metric from eigenvalue decomposition |
| eq:mt-null-radial | `sec:kerr-wormhole` | $\dot{\ell}^2 = E^2 - L^2/(b_0^2+\ell^2)$; null geodesic radial equation |
| $V(\ell) = L^2/(b_0^2+\ell^2)$ | `sec:kerr-wormhole` | Effective potential for null geodesics; maximum at $\ell=0$ (throat = photon sphere) |
| $b_c = b_0$ | `sec:kerr-wormhole` | Critical impact parameter for Morris--Thorne; $b < b_0$ → throat passage, $b > b_0$ → deflection |
| $v^\mu$ (auxiliary) | `sec:geo-formulations` | Auxiliary velocity variable in Lagrangian first-order system; local to one paragraph, superseded by Hamiltonian formulation. Note: glyph collides with generic timelike vector $v^\mu$ (`sec:gr-stress-energy`); context distinguishes |
| eq:geo-lagrangian-eom | `sec:geo-formulations` | Geodesic equation reproduced from eq:geodesic for ch06 context |
| eq:geo-lagrangian-first-order | `sec:geo-formulations` | First-order Lagrangian system; $\dot{x}^\mu = v^\mu$, $\dot{v}^\mu = -\christoffel{\mu}{\alpha}{\beta}v^\alpha v^\beta$ |
| eq:geo-hamiltonian | `sec:geo-formulations` | Super-Hamiltonian reproduced from eq:geodesic-hamiltonian for ch06 context |
| eq:geo-xdot | `sec:geo-formulations` | $\dot{x}^\mu = \inversemetric\,p_\nu$; position equation used throughout ch06 |
| eq:geo-pdot | `sec:geo-formulations` | $\dot{p}_\mu = -\tfrac{1}{2}(\pd{\mu}g^{\alpha\beta})p_\alpha p_\beta$; inverse-metric form |
| eq:geo-pdot-cov | `sec:geo-formulations` | $\dot{p}_\mu = \tfrac{1}{2}(\pd{\mu}g_{\alpha\beta})\dot{x}^\alpha\dot{x}^\beta$; covariant-metric form used throughout ch06 |
| $Q_\xi = p_\mu\,\xi^\mu$ | `sec:geo-constants` | Killing conserved quantity; conserved along geodesics when $\xi^\mu$ is a Killing vector |
| eq:killing-conserved | `sec:geo-constants` | $Q_\xi = p_\mu\,\xi^\mu$; generic Killing conserved quantity |
| eq:geo-energy | `sec:geo-constants` | $E = -p_t$; specific energy from time-translation Killing vector; re-derives eq:schw-energy in Killing framework |
| eq:geo-angmom | `sec:geo-constants` | $L = p_\varphi$; specific angular momentum from axial Killing vector; re-derives eq:schw-angmom |
| $K_{\mu\nu}$ | `sec:geo-constants` | Killing tensor; symmetric $(0,2)$ tensor satisfying $\cd{(\alpha}K_{\mu\nu)} = 0$; generates Carter constant for Kerr |
| eq:killing-tensor | `sec:geo-constants` | $\cd{(\alpha}K_{\mu\nu)} = 0$; Killing tensor equation |
| $\mathcal{Q}$ | `sec:geo-constants` | Carter constant; $\mathcal{Q} = K_{\mu\nu}\dot{x}^\mu\dot{x}^\nu$; fourth constant of motion for Kerr geodesics |
| eq:carter-constant | `sec:geo-constants` | Carter constant explicit form; $\mathcal{Q} = p_\theta^2 + \cos^2\theta(a^2(-\kappa-E^2) + L^2/\sin^2\theta)$ |
| $q = \sqrt{\mathcal{Q}}/E$ | `sec:geo-constants` | Reduced Carter parameter; with $b = L/E$, parametrises photon trajectory on observer's sky |
| $l^\mu$, $n^\mu$ (Kerr principal null) | `sec:geo-constants` | Principal null directions of Kerr geometry; appear in Killing tensor decomposition; local to one equation |
| eq:null-constraint | `sec:geo-null` | $\mathcal{H} = 0$; null geodesic constraint in Hamiltonian language |
| eq:H-dot | `sec:geo-null` | $\d\mathcal{H}/\d\lambda$ chain rule expansion; step in constraint preservation proof |
| eq:H-conservation | `sec:geo-null` | $\d\mathcal{H}/\d\lambda = 0$; constraint preservation for autonomous Hamiltonian systems |
| eq:affine-rescaling | `sec:geo-null` | $p_\mu \to p_\mu/\alpha$; momentum transformation under affine reparametrisation $\lambda \to \alpha\lambda + \beta$ |
| eq:null-constraint-ks | `sec:geo-null` | $\eta^{\mu\nu}p_\mu p_\nu - f(l^\mu p_\mu)^2 = 0$; null constraint in Kerr--Schild coordinates |
| $\alpha$, $\beta$ (affine rescaling) | `sec:geo-null` | Affine reparametrisation constants; $\lambda \to \alpha\lambda + \beta$, $\alpha > 0$; local to one paragraph |
| eq:timelike-constraint | `sec:geo-timelike` | $\mathcal{H} = -\tfrac{1}{2}$; timelike geodesic constraint in Hamiltonian language |
| eq:timelike-H-expanded | `sec:geo-timelike` | Expanded Hamiltonian constraint in equatorial Schwarzschild with $E$, $L$, $p_r$ |
| eq:timelike-radial | `sec:geo-timelike` | $\dot{r}^2 = E^2 - V_{\text{eff}}(r)$; re-derives eq:veff-timelike via Hamiltonian route |
| eq:geo-circular-conditions | `sec:geo-timelike` | Circular orbit conditions: $V_{\text{eff}}(r_c) = E^2$, $V'_{\text{eff}}(r_c) = 0$ |
| $r_c$ | `sec:geo-timelike` | Circular orbit radius; local variable in stability analysis |
| eq:rk45-error | `sec:geo-raytracing` | $e_i = \abs{\delta y_i}/(\epsilon_a + \epsilon_r\abs{y_i})$; mixed absolute-relative error scaling for RK45 |
| eq:rk45-stepcontrol | `sec:geo-raytracing` | Step-size control formula with safety factor, growth clamps, and $(\max_i e_i)^{-1/5}$ exponent |
| $e_i$ | `sec:geo-raytracing` | Scaled error per component; local to step-size discussion |
| $\epsilon_a$, $\epsilon_r$ | `sec:geo-raytracing` | Absolute and relative tolerances; default $10^{-10}$ in codebase |
| $S$, $s_{\min}$, $s_{\max}$ | `sec:geo-raytracing` | Step-size control parameters: safety factor $0.9$, growth bounds $0.2$/$5$ |
| $\gamma_L$ | `sec:geo-raytracing` | Lyapunov exponent of unstable circular photon orbit; $1/(3\sqrt{3}M)$ in coordinate time (Schwarzschild) |
| $\delta y_i$ | `sec:geo-raytracing` | Difference between fifth- and fourth-order RK solutions; local to error estimate |
| eq:H-violation-bound | `sec:geo-conservation` | $\abs{\mathcal{H}(\lambda) - \mathcal{H}_0} \lesssim \epsilon_a$; Hamiltonian constraint violation tracks the tolerance for typical rays |
| eq:EL-drift | `sec:geo-conservation` | Fractional energy and angular momentum drift definitions |
| $\mathcal{H}_0$ | `sec:geo-conservation` | Initial Hamiltonian value; $0$ for null, $-1/2$ for timelike; local to conservation monitoring |
| $\gamma_\lambda$ | `sec:geo-photon-rings` | Lyapunov exponent of photon sphere in affine parameter; $\gamma_\lambda = L/(9M^2)$; coincides with $\d\varphi/\d\lambda$ at $r=3M$. Related to coordinate-time $\gamma_L$ (`sec:geo-raytracing`) by rescaling |
| eq:photon-lyapunov | `sec:geo-photon-rings` | $\delta r(\lambda) \sim e^{\pm\gamma_\lambda\lambda}$; exponential growth/decay of radial perturbations at photon sphere |
| eq:deflection-divergence | `sec:geo-photon-rings` | $\Delta\varphi \approx -\ln(b/b_c - 1) + \text{const}$; logarithmic divergence of deflection angle near critical impact parameter |
| $n$ (sub-ring index) | `sec:geo-photon-rings` | Number of equatorial-plane crossings during close approach; $n=0$ direct, $n=1$ lensing ring, $n \geq 2$ photon ring |
| $\gamma_{\text{ph}}$ | `sec:geo-photon-rings` | Demagnification Lyapunov exponent per half-orbit; $\gamma_{\text{ph}} = \pi$ for Schwarzschild; distinct from SR Lorentz factor $\gamma$ (`sec:sr-lorentz`) and affine exponent $\gamma_\lambda$ |
| eq:demagnification | `sec:geo-photon-rings` | $\delta b_{n+1}/\delta b_n = e^{-\gamma_{\text{ph}}}$; exponential narrowing of photon ring sub-rings |
| $r_{\text{ph}}^{\pm}$ | `sec:geo-photon-rings` | Equatorial prograde/retrograde photon orbit radii in Kerr; eq:kerr-photon-radii |
| eq:kerr-photon-radii | `sec:geo-photon-rings` | $r_{\text{ph}}^{\pm} = 2M(1+\cos(\tfrac{2}{3}\arccos(\mp a_*)))$; Bardeen 1972 |
| $q_c = \sqrt{\mathcal{Q}}/E$ | `sec:geo-photon-rings` | Reduced Carter parameter for critical curve; pairs with $b_c(r)$ to trace shadow boundary. Same quantity as $q$ in `sec:geo-constants` but evaluated on spherical photon orbits |
| $\Delta x$ | `sec:fd-stencils` | Uniform grid spacing (also $\Delta y$, $\Delta z$ for other directions) |
| $x_i = x_0 + i\,\Delta x$ | `sec:fd-stencils` | Grid point position; $f_i = f(x_i)$ |
| $f^{(p)}$ | `sec:fd-stencils` | $p$-th derivative of grid function $f$ |
| $w_k$ / $w_{k_j}$ | `sec:fd-stencils` | Stencil weights for offset $k$ |
| $p$ | `sec:fd-stencils` | Derivative order (context-dependent; reuses glyph from $p$ = pressure in GR chapters) |
| $N$ | `sec:fd-stencils` | Number of stencil points |
| $m$ | `sec:fd-stencils` | Stencil half-width; centred stencil uses $2m+1$ points |
| $N_x$ | `sec:fd-stencils` | Number of grid points in the $x$ direction |
| $\partial$ (Leibniz) | `sec:fd-stencils` | Raw $\partial$ for Leibniz partial derivatives (distinct from `\pd{}` index-notation macro and `\d` total derivative macro) |
| $D_p[f]_i$ | `sec:fd-truncation` | Discrete stencil operator approximating $f^{(p)}_i$ |
| $\tau_i$ | `sec:fd-truncation` | Local truncation error at grid point $i$; $\tau_i = D_p[f]_i - f^{(p)}_i$ |
| $q$ | `sec:fd-truncation` | Order of accuracy ($q = 2m$ for centred stencils) |
| $C_q$ | `sec:fd-truncation` | Leading truncation error coefficient; $\tau_i = C_q\,\Delta x^q\,f^{(p+q)}_i + \ldots$ |
| $Q_R$ | `sec:fd-truncation` | Richardson extrapolant |
| $D_+$, $D_-$ | `sec:fd-dissipation` | Forward and backward undivided difference operators; $D_+ f_i = f_{i+1} - f_i$, $D_- f_i = f_i - f_{i-1}$ |
| $r$ | `sec:fd-dissipation` | Dissipation half-order; $D_+^r D_-^r$ is the $2r$-th order undivided difference |
| $\sigma$ | `sec:fd-dissipation` | Dimensionless dissipation strength parameter; $\sigma > 0$, typical range $0.01$--$0.1$, default $0.05$ |
| $\epsilon_{\text{diss}}$ | `sec:fd-dissipation` | Kreiss--Oliger dissipation term added to RHS of evolution equations |
| $k_{\text{max}} = \pi/\Delta x$ | `sec:fd-dissipation` | Nyquist frequency; maximum resolvable wavenumber on the grid |
| $\epsilon(N_x)$ | `sec:fd-convergence` | Manufactured-solution absolute error at resolution $N_x$ |
| $\rho$ | `sec:fd-convergence` | Convergence ratio $\epsilon(N_x)/\epsilon(2N_x)$; context-local, distinct from energy density $\rho$ (`sec:gr-stress-energy`) |
| $u_4$, $u_2$, $u_1$ | `sec:fd-convergence` | Numerical solutions at relative grid spacings $\Delta x$, $\Delta x/2$, $\Delta x/4$ for self-convergence |
| $\norm{\cdot}_1$, $\norm{\cdot}_2$, $\norm{\cdot}_\infty$ | `sec:fd-convergence` | Grid-function norms ($L^1$, $L^2$, $L^\infty$); scaled by $1/N$ to approximate continuous norms |

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
| Neumann series truncation (null property) | `sec:schw-kerr-schild`, reused `sec:kerr-ks` | Generic metric inverse requires infinite Neumann series; null rank-one perturbation truncates after one term. Maps: explains why KS inverse is a simple sign flip. Breaks: only applies to rank-one perturbations with null vector; Kerr case works because the same structure holds. |
| Potential barrier at throat (wormhole) | `sec:kerr-wormhole` | Effective potential $V(\ell) = L^2/(b_0^2+\ell^2)$ has maximum at throat ($\ell=0$); photons with $b < b_0$ cross the barrier (pass through), $b > b_0$ are reflected (deflect back). Maps: same turning-point analysis as Schwarzschild $V_{\text{eff}}$. Breaks: no capture regime — below-barrier photons pass through rather than being absorbed. |
| Wormhole photon ring = black hole photon ring mechanism | `sec:kerr-wormhole` | Unstable circular orbits at the throat produce a lensing ring by the same mechanism as black hole photon rings. Maps: connects to photon sphere concept from `sec:schw-orbits`. Breaks: wormhole throat replaces photon sphere at finite $r$; no shadow because no capture. |
| Null cone drift / photon acquires mass | `sec:geo-null` | Numerical discretisation error drifts $v^\mu$ off the null cone in Lagrangian system, effectively giving the photon nonzero rest mass. Maps: constraint violation → unphysical mass. Breaks: error is small and reversible; the photon does not literally gain mass. |
| Null constraint as accuracy certificate | `sec:geo-null` | $\mathcal{H}$ acts as a continuous accuracy certificate: zero means healthy, nonzero reveals accumulated error. Maps: checksum / gauge analogy. Breaks: $\mathcal{H}$ drift is monotonic for non-symplectic integrators, not bounded. |
| Rosette pattern (precessing ellipse) | `sec:geo-timelike` | Bound timelike orbits oscillate between turning points like Newtonian ellipses, but the $-2ML^2/r^3$ correction causes perihelion advance, producing a rosette. Maps: connects to Newtonian effective potential analogy from `sec:schw-orbits`. Breaks: only approximately elliptical for weak fields; strong-field orbits can look nothing like an ellipse. |
| Symplectic as bounded-oscillation vs adaptive as monotonic-drift | `sec:geo-raytracing` | Symplectic integrators preserve a nearby Hamiltonian (bounded error oscillations); adaptive RK allows monotonic drift but concentrates work where needed. Maps: tradeoff between global conservation and local accuracy. Breaks: symplectic advantage assumes fixed step; adaptive symplectic methods exist but sacrifice simplicity. |
| Conservation laws as error diagnostics (checksum analogy) | `sec:geo-conservation` | $\mathcal{H}$, $E$, $L$ act as checksums: known values that should remain constant; any drift reveals accumulated integration error. Maps: digital checksum → bit-flip detection; conservation violation → discretisation error detection. Breaks: conservation violations are continuous (not binary pass/fail) and can accumulate gradually. |
| Photon ring as gravitational wide-angle lens | `sec:geo-photon-rings` | $n=1$ sub-ring samples light from the full circumference of the black hole, acting as a wide-angle lens. Maps: explains disproportionate brightness of lensing ring. Breaks: unlike optical lenses, the "focusing" arises from spacetime curvature, not refraction. |
| Self-similar Russian nesting dolls (sub-ring structure) | `sec:geo-photon-rings` | Infinite nested sub-rings, each $e^\pi \approx 23$ times thinner; self-similar structure from Lyapunov instability. Maps: geometric sequence / exponential demagnification. Breaks: not exactly self-similar (Kerr $\gamma_{\text{ph}}$ varies around ring); only logarithmically infinite (unresolvable beyond $n \sim 3$). |
| Discrete analogue of curvature (D2 stencil) | `sec:fd-orders` | Central value's deviation from the average of its two neighbours = discrete curvature. Maps: second derivative measures curvature of $f$. Breaks: only exact for quadratic functions; finite-difference curvature has $\order{\Delta x^2}$ error. |

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
| Inverse metric in geodesic Hamiltonian ($p_\mu \to \dot{x}^\mu$) | `sec:dg-metric` | `sec:geo-formulations` ✓ |
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
| Kerr ISCO prograde efficiency $\eta \approx 42\%$ | `sec:schw-orbits` | `sec:kerr-isco` ✓ |
| Kerr--Schild coordinates for Schwarzschild | `sec:gr-exact-solutions` | `sec:schw-kerr-schild` ✓ |
| Kerr Boyer--Lindquist derivation | `sec:gr-exact-solutions` | `sec:kerr-bl` ✓ |
| AD strategy for Christoffel computation | `sec:gr-exact-solutions` | `ch:autodiff` (TBD) |
| Coordinate singularity resolution at $r=2M$ | `sec:schw-derivation` | `sec:schw-coordinates` ✓ |
| Weak-field identification of $M$ | `sec:schw-derivation` | `sec:gr-weak-field` (backward ref ✓) |
| Kruskal--Szekeres construction and Penrose diagrams | `sec:schw-coordinates` | `sec:schw-kruskal` (TBD) |
| Kerr--Schild coordinates as codebase default | `sec:schw-coordinates` | `sec:schw-kerr-schild` ✓ |
| Kerr--Schild form of Kerr metric | `sec:schw-kerr-schild` | `sec:kerr-ks` ✓ |
| BL quartic derivation and properties | `sec:kerr-bl` | `sec:kerr-bl-quartic` ✓ |
| Frame-dragging consequences | `sec:kerr-bl` | `sec:kerr-horizons` ✓ |
| Horizon-penetrating coordinates for Kerr | `sec:kerr-bl` | `sec:kerr-ks` ✓ |
| AD for Kerr Christoffel symbols | `sec:kerr-ks` | `ch:autodiff` (TBD) |
| Morris--Thorne detailed treatment | `sec:gr-exact-solutions` | `sec:kerr-wormhole` ✓ |
| Conserved quantities as accuracy diagnostics | `sec:geo-constants` | `sec:geo-conservation` ✓ |
| Full numerical integration strategy (adaptive step, Killing vectors, termination) | `sec:dg-geodesic` | `sec:geo-constants` (partial ✓), `sec:geo-conservation` ✓ |
| AD type for exact metric derivatives | `sec:geo-null` | `ch:autodiff` (TBD) |
| $\mathcal{H}$ drift monitoring | `sec:geo-null` | `sec:geo-conservation` ✓ |
| Frequency-shift calculation (Doppler + gravitational) | `sec:geo-timelike` | Camera/rendering chapters (TBD) |
| MHD disc physics | `sec:geo-timelike` | Part~V (TBD) |
| RK theory and order conditions | `sec:geo-raytracing` | `ch:ode-integration` (TBD) |
| AD type for exact metric derivatives | `sec:geo-raytracing` | `ch:autodiff` (TBD) |
| TerminationReason → pixel colour mapping | `sec:geo-raytracing` | `ch:ray-tracing` (TBD) |
| TerminationReason pattern-match → pixel colour | `sec:geo-termination` | `ch:ray-tracing` (TBD) |
| Dense output (Hermite interpolation) for disc crossing | `sec:geo-termination` | `ch:ode-integration` (TBD) |
| Quartic inversion for Kerr radius | `sec:geo-termination` | `sec:kerr-bl-quartic` ✓ |
| Convergence studies via traceGeodesic | `sec:geo-conservation` | `ch:ode-integration` (TBD) |
| Critical curve and shadow shape rendered by ray tracer | `sec:geo-photon-rings` | `sec:geo-raytracing` ✓, `sec:geo-termination` ✓ |
| QNM–photon ring connection (eikonal limit) | `sec:geo-photon-rings` | Not planned (physnote only; gravitational-wave ringdown not in scope) |
| Space VLBI for $n=2$ ring resolution | `sec:geo-photon-rings` | Not planned (observational context; Johnson et al. 2020 reference) |
| Kreiss--Oliger dissipation (7-point stencil, half-width 3) | `sec:fd-stencils` | `sec:fd-dissipation` (drafted) |
| AMR ghost zones and inter-level interpolation | `sec:fd-stencils` | `ch:amr` (TBD) |
| Convergence-testing framework | ch07 intro | `sec:fd-convergence` (TBD), numerical-relativity chapters (TBD) |
| CFL condition forces smaller time steps at finer resolution | `sec:fd-orders` | `ch:ode-integration` (TBD) |
| Lax equivalence theorem — stability analysis and CFL condition | `sec:fd-truncation` | `ch:ode-integration` (TBD) |
| Self-convergence tests verify empirical convergence rate | `sec:fd-truncation` | `sec:fd-convergence` (drafted) |
| Kreiss--Oliger dissipation for stability | `sec:fd-truncation` | `sec:fd-dissipation` (drafted) |
| Convergence tests verify dissipation does not alter convergence rate | `sec:fd-dissipation` | `sec:fd-convergence` (drafted) |
| Ghost-zone depth set by stencil half-width of 3 | `sec:fd-dissipation` | `sec:fd-stencils` (backward ref) |
| BSSN RHS stencil count comparison (12 vs 3 for dissipation) | `sec:fd-dissipation` | `sec:fd-orders` (backward ref) |
| Time-integration order and interaction with spatial accuracy | `sec:fd-convergence` | `ch:ode-integration` (TBD) |
| AMR boundary interaction with convergence testing | `sec:fd-convergence` | `ch:amr` (TBD) |
| Verification chain: time integration, AMR, constraint evolution | `sec:fd-convergence` | `ch:ode-integration`, `ch:amr`, `ch:bssn-ccz4` (all TBD) |

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
| $A$ as azimuthal auxiliary function | $(r^2 + a^2)^2 - a^2\Delta\sin^2\theta$; defined before line element, not after (per review) | `sec:kerr-bl` |
| $r_- = 0$ at $a = 0$ noted as singularity, not Cauchy horizon | In Schwarzschild limit, inner "horizon" coincides with $r = 0$ curvature singularity | `sec:kerr-bl` |
| BL coordinates pedagogical, KS computational | BL used for analytic structure (horizons, limiting cases); KS used by codebase for integration | `sec:kerr-bl` |
| Ingoing KS form (not outgoing) | Ingoing principal null rays are coordinate lines; codebase uses ingoing form; outgoing variant acknowledged but not developed | `sec:kerr-ks` |
| Differential-only KS transformation for Kerr | Unlike Schwarzschild where $\bar{t}$ has a closed-form integral, Kerr KS time is defined only differentially; sufficient for computing the metric | `sec:kerr-ks` |
| physnote on oblate spheroidal: coordinate property, not physical | Euclidean radius $\sqrt{r^2+a^2}$ is a coordinate feature; proper circumference involves full metric factors $\Sigma$, $A$ | `sec:kerr-ks` |
| $p$ disambiguation note at first use | $p^2$ for Euclidean distance collides with pressure ($p$) and momentum ($p_\mu$); parenthetical disambiguation with cross-refs at point of introduction | `sec:kerr-bl-quartic` |
| Ring singularity in Cartesian distance, not circumference | physnote quotes Euclidean radius $\abs{a} \approx 13\;\text{km}$, not the proper circumference (which requires $g_{\varphi\varphi}$ at $\Sigma = 0$) | `sec:kerr-bl-quartic` |
| Biquadratic reduction as explicit pedagogical step | Quartic reduced to quadratic in $u = r^2$ before applying quadratic formula; biquadratic property named at first encounter | `sec:kerr-bl-quartic` |
| Horizon intuition before formalism | One-sentence physical definition of horizon before $g_{rr}$ divergence condition; restores IFI cycle | `sec:kerr-horizons` |
| Cauchy horizon explained in physnote | "Predictability breaks down" unpacked physically (signals from singularity) rather than left as jargon | `sec:kerr-horizons` |
| ZAMO defined by $p_\varphi = 0$ explicitly | "Zero conserved angular momentum" qualifier precedes ZAMO name; distinguishes from generic freely falling observer | `sec:kerr-horizons` |
| "Weak-field post-Newtonian" instead of "gravitomagnetic" | More accessible term for graduate audience; avoids undefined jargon | `sec:kerr-horizons` |
| Penrose process explained in physnote | Brief mechanism (particle splits; negative-energy fragment falls in) rather than bare name-drop | `sec:kerr-horizons` |
| $R(r)$ quartic displayed with derivation sketch | Quartic shown explicitly (eq:kerr-radial-R) so reader can verify E/L formulae; glyph collision with Ricci scalar noted | `sec:kerr-isco` |
| $E_{\text{ISCO}} = 1/\sqrt{3}$ as a limit, not direct evaluation | At exact extremality the formula is $0/0$; the limit $a_* \to 1$ is well defined | `sec:kerr-isco` |
| Infinite throat at extremal degenerate horizon | physnote warns that proper distance from $r > M$ to horizon diverges at $a_* = 1$ | `sec:kerr-isco` |
| $Z_1$, $Z_2$ with inline limiting values | Limiting values at $a_* = 0$ and $a_* = 1$ given immediately after each definition, not deferred to a later paragraph | `sec:kerr-isco` |
| Worked example shows intermediate $Z_1$, $Z_2$ | For $a_* = 0.9$: $Z_1 \approx 1.98$, $Z_2 \approx 2.52$ shown so reader can verify | `sec:kerr-isco` |
| $\rho = \abs{\ell}$ coordinate identification for Morris--Thorne | Codebase uses $\rho = \sqrt{x^2+y^2+z^2} = \abs{\ell}$ (proper distance), NOT circumferential radius $r(\ell) = \sqrt{b_0^2+\ell^2}$; throat at $\rho=0$ with coordinate singularity | `sec:kerr-wormhole` |
| Throat IS photon sphere | Effective potential $V(\ell)$ has maximum at $\ell=0$; unstable circular orbits exist at the throat; lensing ring from same mechanism as black hole photon ring | `sec:kerr-wormhole` |
| Eigenvalue decomposition for MT inverse metric | Radial--transverse split makes inversion algebraic; not "standard matrix inversion" | `sec:kerr-wormhole` |
| Throat geometry analysed in $(\ell,\theta,\varphi)$ chart | Cartesian chart has coordinate singularity at $\rho=0$; metric smooth in proper-distance chart | `sec:kerr-wormhole` |
| Covariant-metric form for Hamiltonian momentum equation | eq:geo-pdot-cov used instead of eq:geo-pdot; derivatives of covariant metric directly accessible via AD | `sec:geo-formulations` |
| Paragraph heading "Derivatives of the covariant metric" | Avoids "covariant-derivative form" which could imply $\nabla_\mu$; names the key computational feature (derivatives of $g_{\alpha\beta}$, not $g^{\alpha\beta}$) | `sec:geo-formulations` |
| No figure in sec:geo-formulations | Purely algebraic/formalism section; no geometric or numerical content requiring a figure | `sec:geo-formulations` |
| \coderef on Spacetime.AutoDiff, not Geodesic.Hamiltonian | sec:geo-null has \coderef{Geodesic}{Hamiltonian}; sec:geo-formulations introduces the AD metric derivative strategy, so \coderef{Spacetime.AutoDiff}{metricDerivativesAD} is placed here | `sec:geo-formulations` |
| Carter constant sign convention $a^2(-\kappa - E^2)$ | Standard Chandrasekhar convention with $\kappa = g_{\mu\nu}\dot{x}^\mu\dot{x}^\nu$; $-\kappa$ maps to rest-mass parameter $\mu^2$ | `sec:geo-constants` |
| Proof via covariant derivative Leibniz rule | Avoids ambiguous $\dot{p}_\mu$ notation; explicit symmetric/antisymmetric contraction argument | `sec:geo-constants` |
| No \coderef in sec:geo-constants | Section is analytical; codebase connection deferred to sec:geo-conservation (monitoring) and sec:geo-null (integration) | `sec:geo-constants` |
| No figure in sec:geo-constants | Purely algebraic section; degree-of-freedom counting and conservation derivations do not require diagrams | `sec:geo-constants` |
| Q removed from codebase monitoring claims | Codebase monitors $E$, $L$, $\mathcal{H}$ but not $\mathcal{Q}$; Carter constant discussed theoretically but not as implemented diagnostic | `sec:geo-constants` |
| Lagrangian constraint preservation stated correctly | Both Lagrangian and Hamiltonian systems preserve the null constraint analytically; the Hamiltonian advantage is diagnostic visibility, not analytical enforcement | `sec:geo-null` |
| $\alpha$, $\beta$ for affine rescaling (not $a$, $b$) | Avoids glyph collision with Kerr spin $a$ and impact parameter $b = L/E$ | `sec:geo-null` |
| Dormand--Prince over symplectic integrators | Adaptive step control and higher order outweigh bounded $\mathcal{H}$ oscillations of symplectic methods; $\mathcal{H}$ drift monitored instead | `sec:geo-null` |
| No figure in sec:geo-null | Algebraic section; numerical monitoring deferred to sec:geo-conservation | `sec:geo-null` |
| $q = \sqrt{\mathcal{Q}}/E$ qualified with $\mathcal{Q} \geq 0$ | Holds for all null geodesics reaching a distant observer; vortical orbits with $\mathcal{Q} < 0$ do not arise for exterior ray tracing | `sec:geo-null` |
| Interpolation parameter $s$ not $t$ for disc crossing | Avoids glyph collision with time coordinate $t$; standard fraction notation | `sec:geo-termination` |
| Linear interpolation for disc crossing ($\order{h^2}$) | Formally below RK45 local accuracy $\order{h^5}$; dense output not implemented | `sec:geo-termination` |
| $\delta = 0.01\,M$ horizon buffer | Small enough for sub-pixel shadow shift; large enough to avoid floating-point overflow near singularity | `sec:geo-termination` |
| $r_{\text{sky}} = 500\,M$ default | Residual deflection $\order{M/r_{\text{sky}}} \approx 2 \times 10^{-3}$ rad; negligible at practical resolutions | `sec:geo-termination` |
| $\lambda_{\text{max}} = 5000\,M$ default | Over 100 near-orbits at photon sphere ($\Delta\lambda \approx 33\,M$ per orbit); far more than physical | `sec:geo-termination` |
| RadiusFn abstraction for spacetime-agnostic termination | Same termination logic for Schwarzschild (Euclidean) and Kerr (quartic solver) | `sec:geo-termination` |
| Hamiltonian route to effective potential | Re-derives $V_{\text{eff}}$ from $\mathcal{H} = -\tfrac{1}{2}$ rather than repeating the metric-norm derivation of `sec:schw-orbits`; value-add is showing the systematic reduction procedure | `sec:geo-timelike` |
| $E^2$ (not $E$) in orbit classification | Radial equation is $\dot{r}^2 = E^2 - V_{\text{eff}}$; orbit types classified by comparing $E^2$ to $V_{\text{eff}}$ peak, not $E$ | `sec:geo-timelike` |
| No \coderef in sec:geo-timelike | Codebase integrates null geodesics only; timelike orbit results enter indirectly via disc model parameters (ISCO, four-velocity) | `sec:geo-timelike` |
| Novikov--Thorne zero-stress limitation noted | warnnote flags MHD torques across ISCO as a known limitation of the thin-disc model | `sec:geo-timelike` |
| Lyapunov exponent quoted in coordinate time | $\gamma_L = 1/(3\sqrt{3}M)$ is the standard Cardoso et al. (2009) result in coordinate time $t$; affine-parameter exponent depends on $E$/$L$ normalisation, less canonical | `sec:geo-raytracing` |
| Step-control equations kept in sec:geo-raytracing | Needed for photon-sphere narrative; full RK theory deferred to ch:ode-integration via xrefnote | `sec:geo-raytracing` |
| Exponent inlined as $-1/5$ not $-1/p$ | Avoids glyph collision with momentum $p_\mu$; more concrete for the reader | `sec:geo-raytracing` |
| "Standard symplectic methods" qualifier | Acknowledges existence of adaptive symplectic methods (time-transformation techniques) without digression | `sec:geo-raytracing` |
| LTE order $\order{h^6}$ for propagated 5th-order solution | Dormand--Prince propagates the 5th-order solution (local extrapolation); LTE $= \order{h^6}$, global error $\sim h^5$; error *estimate* $\delta y \sim h^5$ | `sec:geo-conservation` |
| No abort on constraint violation | Tolerances set conservatively; monitoring is post-hoc validation, not per-ray abort | `sec:geo-conservation` |
| Three-diagnostic cross-check ($\mathcal{H}$, $E$, $L$) | $\mathcal{Q}$ not monitored in codebase; $E$ and $L$ complement $\mathcal{H}$ by probing different failure modes | `sec:geo-conservation` |
| $L = x\,p_y - y\,p_x$ in KS Cartesian | Chain-rule transformation from Cartesian momenta to Boyer--Lindquist $p_\varphi$ | `sec:geo-conservation` |
| `TerminationReason` ADT | `sec:geo-termination` | Algebraic data type encoding all stopping reasons; 6 constructors (HitHorizon, HitCelestialSphere, MaxAffineReached, StepSizeTooSmall, HitAccretionDisk, OutOfGrid) |
| $\delta$ (horizon buffer) | `sec:geo-termination` | Small buffer added to horizon radius for termination; default $0.01\,M$; eq:horizon-buffer |
| $r_{\text{sky}}$ | `sec:geo-termination` | Celestial sphere radius for escape termination; default $500\,M$ |
| $r_{\text{in}}$, $r_{\text{out}}$ | `sec:geo-termination` | Inner and outer radii of accretion disc annulus; $r_{\text{in}}$ typically set to $r_{\text{ISCO}}$ |
| $s$ (disc crossing fraction) | `sec:geo-termination` | Interpolation parameter $s = z_0/(z_0 - z_1)$ for equatorial-plane crossing; eq:disk-crossing-frac. Note: $s$ chosen to avoid glyph collision with time $t$ |
| eq:disk-crossing-interp | `sec:geo-termination` | Linear interpolation of position and momentum at disc crossing |
| $\lambda_{\text{max}}$ | `sec:geo-termination` | Maximum affine parameter for safety-net termination; default $5000\,M$ |
| $h_{\min}$ | `sec:geo-termination` | Minimum step size for safety-net termination; default $10^{-12}$ |
| `RadiusFn` | `sec:geo-termination` | Abstraction: function from position to scalar radius; Euclidean for Schwarzschild, quartic solver for Kerr |
| $\gamma_{\text{ph}}$ for demagnification exponent (not bare $\gamma$) | Avoids collision with SR Lorentz factor $\gamma$ (`sec:sr-lorentz`) and affine Lyapunov exponent $\gamma_\lambda$ | `sec:geo-photon-rings` |
| $\gamma_\lambda$ bridge to $\gamma_L$ via physnote | Connects affine Lyapunov exponent (this section) to coordinate-time exponent (`sec:geo-raytracing`) without breaking section flow | `sec:geo-photon-rings` |
| "Factor of three" for Kerr demagnification variation | Ratio $\sim 50/15 \approx 3.3$ at $a_* = 0.9$; physicist review corrected from "factor of two" | `sec:geo-photon-rings` |
| "determines" not "equals" for QNM physnote | Lyapunov exponent determines (sets) the QNM imaginary part via eikonal correspondence; strict equality requires careful normalisation | `sec:geo-photon-rings` |
| No \coderef in sec:geo-photon-rings | \starmark section is analytical/observational; codebase connection made via implnote (ray tracer captures sub-rings implicitly) | `sec:geo-photon-rings` |
| Centred stencil order claim restricted to $p \leq 2$ | General formula differs for $p \geq 3$; book only uses first and second derivatives | `sec:fd-stencils` |
| Separable mixed partial: cache benefit, not access-count reduction | Both passes access 25 grid points (same as full 2D stencil); advantage is structured row access patterns and implementation simplicity | `sec:fd-stencils` |
| Boundary order qualified (Gustafsson) | One-sided stencils \emph{can} reduce global order; hyperbolic problems may preserve interior order with $q-1$ boundary scheme | `sec:fd-stencils` |
| Ghost zones introduced before AMR chapter | Concept defined here; full AMR treatment deferred to `ch:amr` | `sec:fd-stencils` |
| Worked example uses $f(x)=\sin(2\pi x)$, $N_x=20$ | Concrete numbers ground the error analysis; same function appears in codebase convergence tests | `sec:fd-orders` |
| BSSN stencil count 3+3+3×2=12 per field per grid point | 3 first derivatives + 3 second derivatives + 3 mixed pairs × 2 passes each | `sec:fd-orders` |
| Order-of-magnitude $10^{-6}$ target error comparison ignores prefactors | General argument (not tied to specific test function); prefactors are O(1) | `sec:fd-orders` |
| ADM variables rendered with macros in closing paragraph | $\conformal$, $\extrinsic$, $\lapse$, $\shift$ | `sec:fd-orders` |
| $C_q$ presented as $\abs{C_q}$ to match fd-orders convention | Sign of $C_q$ is negative for D1 and D2 fourth-order stencils; fd-orders table uses unsigned coefficients | `sec:fd-truncation` |
| Richardson extrapolation emphasised as diagnostic, not accuracy booster | Diagnostic role connects to sec:fd-convergence verification framework | `sec:fd-truncation` |
| $f^{(p+q)}_i \neq 0$ qualifier on convergence ratio | Ratio $2^q$ only meaningful when leading derivative is nonzero | `sec:fd-truncation` |
| Lax equivalence theorem scoped to linear problems | Nonlinearity of BSSN acknowledged via warnnote; empirical convergence cited | `sec:fd-truncation` |
| Richardson worked example reuses $\sin(2\pi x)$ from fd-orders | Continuity with previous worked comparison; error $\sim 3 \times 10^{-6}$ | `sec:fd-truncation` |
| $r = 3$ (fifth-order) dissipation for fourth-order spatial scheme | Minimum $r$ satisfying $2r - 1 \geq q = 4$; preserves convergence order | `sec:fd-dissipation` |
| Sign convention $(-1)^{r+1}$ in KO operator | Ensures universally negative transfer function for all $r$; sign chain $(-1)^{r+1} \cdot (-1)^r = -1$ made explicit | `sec:fd-dissipation` |
| Normalisation $2^{2r}$ in KO operator | Maximum dissipation rate at Nyquist equals $\sigma/\Delta x$; stencil coefficients are binomial/$2^{2r}$ | `sec:fd-dissipation` |
| Codebase stencil $[-1,6,-15,20,-15,6,-1]/64$ noted as $-D_+^3 D_-^3/64$ | Negated relative to standard convention; absorbed into calling convention per implnote | `sec:fd-dissipation` |
| $\sigma = 0.05$ default | Mid-range of typical $0.01$--$0.1$; effective noise suppression without visible accuracy loss | `sec:fd-dissipation` |
| Separable 3D dissipation (sum of 1D operators) | No cross-derivative terms; cost = 3 × 7-point stencils per grid point | `sec:fd-dissipation` |
| Convergence test acceptance window $[12, 20]$ for ratio $16$ | Deliberately wide to catch order-of-magnitude bugs, not precision measurement | `sec:fd-convergence` |
| $\sin(2\pi x)$ reused as manufactured-solution test function | Continuity with fd-orders and fd-truncation worked examples; $f^{(5)}(0.5) \neq 0$ avoids vanishing-coefficient pitfall | `sec:fd-convergence` |
| Self-convergence subscript convention: $u_4$, $u_2$, $u_1$ by relative spacing | Subscript = relative grid spacing factor; coarsest grid points are subset of all three | `sec:fd-convergence` |
| $L^2$ norm as default for convergence monitoring | Resolution-independent, averages over grid; $L^\infty$ reserved for localised-error detection | `sec:fd-convergence` |
| Grid-function norms scaled by $1/N$ | Approximate continuous $L^p$ norms; remain bounded as $N \to \infty$ | `sec:fd-convergence` |
| Verification chain metaphor for cross-chapter testing | Each chapter adds a link; pattern: predict rate, measure, treat discrepancy as bug | `sec:fd-convergence` |
