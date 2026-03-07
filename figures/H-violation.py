"""Hamiltonian constraint violation for null geodesics near the photon sphere.

Generates figures/H-violation.pgf for inclusion in sec:geo-conservation.

Integrates the full 8-component Hamiltonian system in Cartesian
Kerr-Schild coordinates for Schwarzschild (matching the codebase approach):
  dx^mu/dlambda = g^{mu nu} p_nu
  dp_mu/dlambda = -(1/2)(d_mu g^{ab}) p_a p_b

The Hamiltonian H = (1/2) g^{mu nu} p_mu p_nu should vanish identically
for null geodesics; any departure is pure discretisation error.

Three equatorial null geodesics:
  (a) Far ray        — b = 8M    (gold, deflected)
  (b) Near-critical  — b ≈ b_c   (blue, winds near photon sphere)
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


# ---- Schwarzschild Kerr-Schild metric (analytical) ----

def ks_inverse_metric(pos):
    """Schwarzschild KS inverse metric g^{mu nu}.

    g^{mu nu} = eta^{mu nu} - H l^mu l^nu
    where H = 2M/r, l^mu = (-1, x/r, y/r, z/r).
    """
    t, x, y, z = pos
    r = np.sqrt(x**2 + y**2 + z**2)
    if r < 1e-10:
        r = 1e-10
    H = 2.0 * M / r
    l_up = np.array([-1.0, x / r, y / r, z / r])

    eta_inv = np.diag([-1.0, 1.0, 1.0, 1.0])
    ginv = eta_inv - H * np.outer(l_up, l_up)
    return ginv


def inverse_metric_derivatives(pos):
    """Analytical derivatives d_mu g^{ab} for Schwarzschild KS.

    g^{mu nu} = eta^{mu nu} - (2M/r) l^mu l^nu
    where l^mu = (-1, x^i/r) with i=1,2,3.

    d_mu g^{ab} = -d_mu(H) l^a l^b - H d_mu(l^a) l^b - H l^a d_mu(l^b)

    H = 2M/r => d_t H = 0, d_i H = -2M x^i / r^3

    l^0 = -1 => d_mu l^0 = 0
    l^i = x^i/r => d_t l^i = 0, d_j l^i = delta^i_j/r - x^i x^j/r^3
    """
    t, x, y, z = pos
    r2 = x**2 + y**2 + z**2
    r = np.sqrt(r2)
    if r < 1e-10:
        r = 1e-10
        r2 = r**2
    r3 = r * r2

    H = 2.0 * M / r
    xi = np.array([x, y, z])  # spatial position
    l_up = np.array([-1.0, x / r, y / r, z / r])

    derivs = []

    # d/dt: H doesn't depend on t, l doesn't depend on t
    derivs.append(np.zeros((4, 4)))

    # d/dx^j for j = 1, 2, 3
    for j in range(3):
        dg = np.zeros((4, 4))

        # d_j H = -2M x^j / r^3
        dH = -2.0 * M * xi[j] / r3

        # d_j l^a: l^0 = -1 (const), l^i = x^i/r
        dl = np.zeros(4)
        for i in range(3):
            dl[i + 1] = (1.0 if i == j else 0.0) / r - xi[i] * xi[j] / r3

        for a in range(4):
            for b in range(4):
                dg[a, b] = -(dH * l_up[a] * l_up[b]
                             + H * dl[a] * l_up[b]
                             + H * l_up[a] * dl[b])

        derivs.append(dg)

    return derivs


# ---- Hamiltonian system ----

def hamiltonian_rhs(lam, y):
    """Full 8-component Hamiltonian RHS.

    y = [t, x, y, z, p_t, p_x, p_y, p_z]

    dx^mu/dlambda = g^{mu nu} p_nu
    dp_mu/dlambda = -(1/2)(d_mu g^{ab}) p_a p_b
    """
    pos = y[:4]
    mom = y[4:]

    ginv = ks_inverse_metric(pos)

    # xdot^mu = g^{mu nu} p_nu
    xdot = ginv @ mom

    # dp_mu/dlambda = -(1/2)(d_mu g^{ab}) p_a p_b
    dginv = inverse_metric_derivatives(pos)
    pdot = np.zeros(4)
    for mu in range(4):
        pdot[mu] = -0.5 * mom @ dginv[mu] @ mom

    return np.concatenate([xdot, pdot])


def hamiltonian_value(pos, mom):
    """H = (1/2) g^{mu nu} p_mu p_nu."""
    ginv = ks_inverse_metric(pos)
    return 0.5 * mom @ ginv @ mom


def setup_initial_conditions(b, r0):
    """Set up null geodesic initial conditions in KS Cartesian.

    Photon starts at (t=0, x=r0, y=0, z=0) moving in -x direction
    with impact parameter b (angular momentum L = b, energy E = 1).
    """
    pos = np.array([0.0, r0, 0.0, 0.0])

    p_t = -1.0
    p_y = b / r0
    p_z = 0.0

    ginv = ks_inverse_metric(pos)
    # H = 0 => quadratic in p_x
    A = ginv[1, 1]
    B = 2.0 * (ginv[0, 1] * p_t + ginv[1, 2] * p_y)
    C = (ginv[0, 0] * p_t**2 + 2.0 * ginv[0, 2] * p_t * p_y
         + ginv[2, 2] * p_y**2)

    disc = B**2 - 4.0 * A * C
    if disc < 0:
        disc = 0.0

    # Choose root corresponding to inward-moving ray
    p_x1 = (-B + np.sqrt(disc)) / (2.0 * A)
    p_x2 = (-B - np.sqrt(disc)) / (2.0 * A)
    xdot1 = ginv[1, :] @ np.array([p_t, p_x1, p_y, p_z])
    xdot2 = ginv[1, :] @ np.array([p_t, p_x2, p_y, p_z])
    p_x = p_x1 if xdot1 < 0 else p_x2

    mom = np.array([p_t, p_x, p_y, p_z])
    return np.concatenate([pos, mom])


def integrate_full(b, r0, lam_max, r_stop=2.1,
                   atol=1e-10, rtol=1e-10):
    """Integrate a full 8-component null geodesic and record |H|."""
    y0 = setup_initial_conditions(b, r0)

    # Verify initial H
    H0 = hamiltonian_value(y0[:4], y0[4:])
    print(f"  Initial H = {H0:.2e}")

    solver = RK45(hamiltonian_rhs, 0.0, y0, lam_max,
                  rtol=rtol, atol=atol, max_step=np.inf)

    lambdas = [0.0]
    H_values = [abs(H0)]

    while solver.status == "running":
        solver.step()
        if solver.status == "failed":
            break

        pos = solver.y[:4]
        mom = solver.y[4:]
        r = np.sqrt(pos[1]**2 + pos[2]**2 + pos[3]**2)

        lambdas.append(solver.t)
        H_values.append(abs(hamiltonian_value(pos, mom)))

        if r < r_stop or r > 80.0:
            break

    return np.array(lambdas), np.array(H_values)


# ---- Integrate three rays ----

b_c = 3.0 * np.sqrt(3.0) * M  # ≈ 5.1962M
r_start = 50.0

print("Far ray (b = 8M):")
b_far = 8.0 * M
lam_far, H_far = integrate_full(b_far, r_start, lam_max=500.0)
print(f"  {len(H_far)} pts, |H|: [{H_far.min():.2e}, {H_far.max():.2e}]")

print("Near-critical ray (b ≈ b_c):")
b_near = b_c + 1e-4
lam_near, H_near = integrate_full(b_near, r_start, lam_max=3000.0)
print(f"  {len(H_near)} pts, |H|: [{H_near.min():.2e}, {H_near.max():.2e}]")

print("Plunge ray (b = 4M):")
b_plunge = 4.0 * M
lam_plunge, H_plunge = integrate_full(
    b_plunge, r_start, lam_max=500.0, r_stop=2.5)
print(f"  {len(H_plunge)} pts, |H|: [{H_plunge.min():.2e}, {H_plunge.max():.2e}]")


# ---- Plot ----

fig, ax = plt.subplots(figsize=(ehplot.TEXT_WIDTH, 0.55 * ehplot.TEXT_WIDTH))

ax.semilogy(lam_far, H_far, color=ehplot.GOLD, linewidth=0.8,
            label=r"$b = 8M$")
ax.semilogy(lam_near, H_near, color=ehplot.BLUE, linewidth=0.8,
            label=r"$b \approx b_c$")
ax.semilogy(lam_plunge, H_plunge, color=ehplot.CRIMSON,
            linewidth=0.8, label=r"$b = 4M$")

# Tolerance reference line
lam_max_plot = max(lam_far[-1], lam_near[-1], lam_plunge[-1])
ax.axhline(y=1e-10, color=ehplot.GRAY, linewidth=0.5,
           linestyle="--", zorder=0)
ax.text(lam_max_plot * 0.98, 1.6e-10, r"$\epsilon = 10^{-10}$",
        color=ehplot.GRAY, fontsize=6, ha="right", va="bottom")

ax.set_xlabel(r"$\lambda$")
ax.set_ylabel(r"$|\mathcal{H}|$")
ax.legend(loc="lower right", fontsize=6.5, framealpha=0.85)

fig.tight_layout()

# ---- Save ----

out = Path(__file__).parent / "H-violation.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"\nWrote {out}")
