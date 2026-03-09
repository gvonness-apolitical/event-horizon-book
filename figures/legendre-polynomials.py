"""Legendre polynomials P_0 through P_5 with LGL nodes.

Generates figures/legendre-polynomials.pgf for inclusion in sec:spec-legendre.

Plots the first six Legendre polynomials on [-1,1] evaluated on a 500-point
fine grid, with Legendre-Gauss-Lobatto nodes for N=5 marked as dots on the
x-axis.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np


# --- Legendre polynomial evaluation via Bonnet recurrence ---

def legendre(n, x):
    """Evaluate P_n(x) using the Bonnet three-term recurrence."""
    if n == 0:
        return np.ones_like(x, dtype=float)
    p_prev = np.ones_like(x, dtype=float)   # P_0
    p_curr = x.copy()                        # P_1
    for k in range(1, n):
        p_next = ((2*k + 1) * x * p_curr - k * p_prev) / (k + 1)
        p_prev = p_curr
        p_curr = p_next
    return p_curr


def legendre_and_deriv(n, x):
    """Evaluate P_n(x) and P_n'(x) simultaneously."""
    if n == 0:
        return 1.0, 0.0
    p_prev, p_curr = 1.0, x
    dp_prev, dp_curr = 0.0, 1.0
    for k in range(1, n):
        p_next = ((2*k + 1) * x * p_curr - k * p_prev) / (k + 1)
        dp_next = ((2*k + 1) * (p_curr + x * dp_curr) - k * dp_prev) / (k + 1)
        p_prev, p_curr = p_curr, p_next
        dp_prev, dp_curr = dp_curr, dp_next
    return p_curr, dp_curr


# --- LGL nodes via Newton iteration on P_N' ---

def lgl_nodes(N):
    """Compute N+1 Legendre-Gauss-Lobatto nodes."""
    nodes = np.empty(N + 1)
    nodes[0] = -1.0
    nodes[N] = 1.0
    for i in range(1, N):
        # Initial guess from Chebyshev extrema
        x = -np.cos(i * np.pi / N)
        for _ in range(50):
            p, dp = legendre_and_deriv(N, x)
            # Legendre ODE: (1-x^2)P'' = 2xP' - N(N+1)P
            d2p = (2.0 * x * dp - N * (N + 1) * p) / (1.0 - x * x)
            dx = dp / d2p
            x -= dx
            if abs(dx) < 1e-15:
                break
        nodes[i] = x
    return nodes


# --- Fine evaluation grid ---
x_fine = np.linspace(-1, 1, 500)

# --- Colours and styles for six polynomials ---
# P_0, P_1 are visually simple; use thin gray with dashes
# P_2..P_5 get the four palette colours
styles = [
    {"color": ehplot.GRAY, "linewidth": 0.8, "linestyle": (0, (4, 3)),
     "alpha": 0.6},                                           # P_0
    {"color": ehplot.GRAY, "linewidth": 0.8, "linestyle": (0, (2, 2)),
     "alpha": 0.6},                                           # P_1
    {"color": ehplot.GOLD,    "linewidth": 1.2, "linestyle": "-"},  # P_2
    {"color": ehplot.BLUE,    "linewidth": 1.2, "linestyle": "-"},  # P_3
    {"color": ehplot.CRIMSON, "linewidth": 1.2, "linestyle": "-"},  # P_4
    {"color": ehplot.GRAY,    "linewidth": 1.2, "linestyle": "-"},  # P_5
]

# --- Plot ---
fig, ax = plt.subplots(figsize=(ehplot.TEXT_WIDTH, 2.5))

for n in range(6):
    y = legendre(n, x_fine)
    ax.plot(x_fine, y, label=rf"$P_{n}$", zorder=3, **styles[n])

# LGL nodes for N=5 on the x-axis
nodes = lgl_nodes(5)
ax.plot(nodes, np.zeros_like(nodes), "o", color="k", markersize=3.5,
        zorder=5, clip_on=False, label="LGL nodes")

# Light horizontal line at y=0
ax.axhline(0, color="k", linewidth=0.3, zorder=1)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$P_n(x)$")
ax.set_xlim(-1, 1)
ax.set_ylim(-1.1, 1.1)

ax.legend(loc="lower left", fontsize=6, ncol=4, columnspacing=1.0)

# --- Save ---
out = Path(__file__).parent / "legendre-polynomials.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
