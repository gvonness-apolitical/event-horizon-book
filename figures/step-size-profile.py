"""Adaptive step-size profiles for null geodesics near the photon sphere.

Generates figures/step-size-profile.pgf for inclusion in sec:geo-raytracing.

Uses scipy's RK45 solver in manual stepping mode to record per-step sizes
for three null geodesics in the Schwarzschild geometry (equatorial plane):
  (a) Far ray        — b = 8M    (gold, deflected at r ≈ 6.7M)
  (b) Near-critical  — b ≈ b_c   (blue, winds near photon sphere at r ≈ 3M)
  (c) Plunge ray     — b = 4M    (crimson, crosses horizon)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import RK45


M = 1.0


def null_geodesic_rhs(lam, y):
    """RHS for equatorial null geodesic: y = [r, phi, r_dot].

    We set E = 1, L = b (impact parameter).
    """
    r, phi, rdot = y
    b = null_geodesic_rhs.b

    if r <= 2.0 * M:
        return np.array([0.0, 0.0, 0.0])

    # V'_eff = 2b^2/r^3 (3M/r - 1)
    veff_prime = 2.0 * b**2 / r**3 * (3.0 * M / r - 1.0)
    return np.array([rdot, b / r**2, -veff_prime / 2.0])


def integrate_with_stepsizes(b, r0, lam_max, r_stop=2.1,
                              atol=1e-10, rtol=1e-10):
    """Integrate a null geodesic and record step sizes."""
    null_geodesic_rhs.b = b
    veff = (1.0 - 2.0 * M / r0) * b**2 / r0**2
    rdot0 = -np.sqrt(max(1.0 - veff, 0.0))
    y0 = np.array([r0, 0.0, rdot0])

    solver = RK45(null_geodesic_rhs, 0.0, y0, lam_max,
                  rtol=rtol, atol=atol, max_step=np.inf)

    lambdas = [0.0]
    step_sizes = []
    r_values = [r0]

    while solver.status == "running":
        solver.step()
        if solver.status == "failed":
            break

        r = solver.y[0]
        lambdas.append(solver.t)
        step_sizes.append(solver.t - lambdas[-2])
        r_values.append(r)

        if r < r_stop or r > 80.0:
            break

    return np.array(lambdas), np.array(step_sizes), np.array(r_values)


# ---- Integrate three rays ----

b_c = 3.0 * np.sqrt(3.0) * M  # ≈ 5.1962M
r_start = 50.0

# (a) Far ray: b = 8M — deflected, turns at r ≈ 6.7M
b_far = 8.0 * M
lam_far, h_far, r_far = integrate_with_stepsizes(
    b_far, r_start, lam_max=500.0)
print(f"Far (b={b_far}M): {len(h_far)} steps, "
      f"r: [{r_far.min():.2f}, {r_far.max():.2f}], "
      f"h: [{h_far.min():.4f}, {h_far.max():.2f}]")

# (b) Near-critical: b just above b_c — winds near r = 3M
b_near = b_c + 1e-4
lam_near, h_near, r_near = integrate_with_stepsizes(
    b_near, r_start, lam_max=3000.0)
print(f"Near-critical (b={b_near:.4f}M): {len(h_near)} steps, "
      f"r: [{r_near.min():.4f}, {r_near.max():.2f}], "
      f"h: [{h_near.min():.4f}, {h_near.max():.2f}]")

# (c) Plunge ray: b = 4M — crosses barrier, hits horizon
b_plunge = 4.0 * M
lam_plunge, h_plunge, r_plunge = integrate_with_stepsizes(
    b_plunge, r_start, lam_max=500.0, r_stop=2.5)
print(f"Plunge (b={b_plunge}M): {len(h_plunge)} steps, "
      f"r: [{r_plunge.min():.3f}, {r_plunge.max():.2f}], "
      f"h: [{h_plunge.min():.4f}, {h_plunge.max():.2f}]")


# ---- Plot ----

fig, ax = plt.subplots(figsize=(ehplot.TEXT_WIDTH, 0.55 * ehplot.TEXT_WIDTH))

# Midpoint lambda for each step
def midpoints(lam):
    return 0.5 * (lam[:-1] + lam[1:])

ax.semilogy(midpoints(lam_far), h_far, color=ehplot.GOLD, linewidth=0.8,
            label=r"$b = 8M$")
ax.semilogy(midpoints(lam_near), h_near, color=ehplot.BLUE, linewidth=0.8,
            label=r"$b \approx b_c$")
ax.semilogy(midpoints(lam_plunge), h_plunge, color=ehplot.CRIMSON,
            linewidth=0.8, label=r"$b = 4M$")

ax.set_xlabel(r"$\lambda$")
ax.set_ylabel(r"$h$")
ax.legend(loc="center right", fontsize=6.5, framealpha=0.85)

fig.tight_layout()

# ---- Save ----

out = Path(__file__).parent / "step-size-profile.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"\nWrote {out}")
