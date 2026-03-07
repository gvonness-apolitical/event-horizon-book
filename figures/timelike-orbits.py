"""Three representative timelike orbits in the Schwarzschild geometry.

Generates figures/timelike-orbits.pgf for inclusion in sec:geo-timelike.

Orbits plotted as Cartesian projections (x, y) of the equatorial plane:
  (a) Bound precessing orbit  — L/M = 4.0, low eccentricity, ~5 orbits
  (b) Marginal orbit          — L/M = 4.0, E^2 = V_max (asymptotic spiral)
  (c) Plunge orbit            — L/M = 3.7, E = 0.97 (exceeds barrier)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


M = 1.0


def veff(r, L):
    """Schwarzschild timelike effective potential V_eff(r)."""
    return (1.0 - 2.0 * M / r) * (1.0 + L**2 / r**2)


def veff_prime(r, L):
    """dV_eff/dr."""
    return (2.0 * M / r**2) * (1.0 + L**2 / r**2) + \
           (1.0 - 2.0 * M / r) * (-2.0 * L**2 / r**3)


def geodesic_rhs(tau, y, E, L):
    """RHS for [dr/dtau, dphi/dtau, d^2r/dtau^2].

    State y = [r, phi, rdot].
    From rdot^2 = E^2 - V_eff(r), differentiate: rddot = -V'_eff / 2.
    """
    r, phi, rdot = y
    if r <= 2.0 * M + 1e-6:
        return [0.0, 0.0, 0.0]
    phidot = L / r**2
    rddot = -veff_prime(r, L) / 2.0
    return [rdot, phidot, rddot]


def horizon_event(tau, y, E, L):
    """Stop integration when r approaches the horizon."""
    return y[0] - 2.0 * M - 1e-4

horizon_event.terminal = True
horizon_event.direction = -1


def integrate_orbit(r0, rdot0, E, L, tau_max, max_step=0.05):
    """Integrate a timelike geodesic starting at (r0, phi=0, rdot0)."""
    sol = solve_ivp(
        geodesic_rhs, [0, tau_max], [r0, 0.0, rdot0],
        args=(E, L), method="DOP853", rtol=1e-13, atol=1e-15,
        max_step=max_step, events=horizon_event,
    )
    return sol.y[0], sol.y[1]


# --- Orbit parameters ---

L_circ = 4.0 * M  # shared angular momentum for bound and marginal

# Critical radii for L = 4M
def vp_circ(r):
    return veff_prime(r, L_circ)

r_stable = brentq(vp_circ, 6.0, 30.0)    # stable circular orbit (12M)
r_unstable = brentq(vp_circ, 3.0, 5.5)    # unstable circular orbit (4M)
E2_min = veff(r_stable, L_circ)            # V_eff at stable minimum
E2_max = veff(r_unstable, L_circ)          # V_eff at unstable maximum


# --- Orbit (a): Bound precessing ---
# Low eccentricity for compact rosette with visible precession
E2_bound = E2_min + 0.08 * (E2_max - E2_min)
E_bound = np.sqrt(E2_bound)

# Start at apoapsis (rdot = 0)
def radial_zero_outer(r):
    return veff(r, L_circ) - E2_bound

r_apo = brentq(radial_zero_outer, r_stable, 80.0)
r_bound, phi_bound = integrate_orbit(r_apo, 0.0, E_bound, L_circ,
                                     tau_max=1500.0, max_step=0.5)


# --- Orbit (b): Marginal (E^2 = V_max exactly) ---
# Start at r = 10M, inward; asymptotically approaches r_unstable = 4M.
E_marg = np.sqrt(E2_max)
r_start_marg = 10.0
rdot_marg = -np.sqrt(max(E2_max - veff(r_start_marg, L_circ), 0.0))
r_marg, phi_marg = integrate_orbit(r_start_marg, rdot_marg, E_marg,
                                   L_circ, tau_max=800.0, max_step=0.05)

# Clip at numerical bounce: find where r starts increasing after settling
# near r_unstable.  Keep only the clean inward spiral.
below_threshold = np.where(r_marg < r_unstable + 0.1)[0]
if len(below_threshold) > 0:
    first_near = below_threshold[0]
    bounce = np.where(r_marg[first_near:] > r_unstable + 0.5)[0]
    clip_idx = (first_near + bounce[0]) if len(bounce) > 0 else len(r_marg)
else:
    clip_idx = len(r_marg)

# Keep a few windings at r_unstable but not too many (diminishing visual return)
max_phi_marg = phi_marg[below_threshold[0]] + 3.0 * 2 * np.pi if len(below_threshold) > 0 else phi_marg[-1]
phi_clip = np.where(phi_marg[:clip_idx] <= max_phi_marg)[0]
clip_idx = phi_clip[-1] + 1 if len(phi_clip) > 0 else clip_idx

r_marg = r_marg[:clip_idx]
phi_marg = phi_marg[:clip_idx]


# --- Orbit (c): Plunge ---
# L/M = 3.7 with E^2 above the barrier — particle crosses and plunges
L_plunge = 3.7 * M
E_plunge = 0.97
E2_plunge = E_plunge**2

r_start_plunge = 20.0
rdot_plunge = -np.sqrt(max(E2_plunge - veff(r_start_plunge, L_plunge), 0.0))
r_plunge, phi_plunge = integrate_orbit(r_start_plunge, rdot_plunge,
                                       E_plunge, L_plunge, tau_max=200.0,
                                       max_step=0.05)


# --- Convert to Cartesian ---
def to_xy(r, phi):
    return r * np.cos(phi), r * np.sin(phi)

x_b, y_b = to_xy(r_bound, phi_bound)
x_m, y_m = to_xy(r_marg, phi_marg)
x_p, y_p = to_xy(r_plunge, phi_plunge)


# --- Plot ---
fig, ax = plt.subplots(figsize=(ehplot.TEXT_WIDTH, ehplot.TEXT_WIDTH))

# Reference circles
theta_circ = np.linspace(0, 2 * np.pi, 300)
ax.plot(2.0 * np.cos(theta_circ), 2.0 * np.sin(theta_circ),
        color=ehplot.GRAY, linestyle="--", linewidth=0.6, alpha=0.5)
ax.plot(6.0 * np.cos(theta_circ), 6.0 * np.sin(theta_circ),
        color=ehplot.GRAY, linestyle=":", linewidth=0.6, alpha=0.5)

# Fill horizon
ax.fill(2.0 * np.cos(theta_circ), 2.0 * np.sin(theta_circ),
        color="black", alpha=0.12, zorder=0)

# Orbits
ax.plot(x_b, y_b, color=ehplot.GOLD, linewidth=0.8,
        label="Bound (precessing)", zorder=2)
ax.plot(x_m, y_m, color=ehplot.BLUE, linewidth=0.8,
        label="Marginal", zorder=2)
ax.plot(x_p, y_p, color=ehplot.CRIMSON, linewidth=0.8,
        label="Plunge", zorder=2)

# Starting dots
ax.plot(x_b[0], y_b[0], "o", color=ehplot.GOLD, markersize=2.5, zorder=3)
ax.plot(x_m[0], y_m[0], "o", color=ehplot.BLUE, markersize=2.5, zorder=3)
ax.plot(x_p[0], y_p[0], "o", color=ehplot.CRIMSON, markersize=2.5, zorder=3)

# Labels for reference circles
ax.text(1.0, -2.8, r"$2M$", fontsize=6, color=ehplot.GRAY, ha="center",
        alpha=0.7)
ax.text(4.0, -6.8, r"$6M$", fontsize=6, color=ehplot.GRAY, ha="center",
        alpha=0.7)

# Formatting
lim = max(np.max(np.abs(x_b)), np.max(np.abs(y_b)),
          np.max(np.abs(x_p)), np.max(np.abs(y_p))) * 1.08
lim = max(lim, 22.0)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_aspect("equal")
ax.set_xlabel(r"$x / M$")
ax.set_ylabel(r"$y / M$")

ax.legend(loc="upper right", fontsize=6.5, framealpha=0.85)

fig.tight_layout()

# --- Save ---
out = Path(__file__).parent / "timelike-orbits.pgf"
fig.savefig(str(out))
plt.close(fig)

print(f"Wrote {out}")
print(f"Bound: r in [{r_bound.min():.2f}, {r_bound.max():.2f}], "
      f"{phi_bound[-1]/(2*np.pi):.1f} orbits")
print(f"Marginal: r in [{r_marg.min():.3f}, {r_marg.max():.2f}], "
      f"{phi_marg[-1]/(2*np.pi):.1f} orbits")
print(f"Plunge: r in [{r_plunge.min():.2f}, {r_plunge.max():.2f}], "
      f"{phi_plunge[-1]/(2*np.pi):.1f} orbits")
