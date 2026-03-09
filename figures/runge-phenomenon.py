"""Runge phenomenon: equidistant vs Chebyshev interpolation.

Generates figures/runge-phenomenon.pgf for inclusion in sec:spec-interpolation.

Panel (a): Runge function f(x) = 1/(1+25x²) on [-1,1] interpolated on
equidistant nodes at N = 5, 10, 15.  Endpoint oscillations grow with N.

Panel (b): Same function interpolated on Chebyshev Gauss-Lobatto nodes.
Uniform convergence across the interval.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np


# --- Runge function ---

def runge(x):
    return 1.0 / (1.0 + 25.0 * x**2)


# --- Lagrange interpolation via barycentric formula ---

def barycentric_weights(nodes):
    """Compute barycentric weights for Lagrange interpolation."""
    n = len(nodes)
    w = np.ones(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                w[i] /= (nodes[i] - nodes[j])
    return w


def lagrange_interp(nodes, fvals, x_eval):
    """Evaluate Lagrange interpolant at x_eval using barycentric formula."""
    w = barycentric_weights(nodes)
    result = np.empty_like(x_eval)

    for k, x in enumerate(x_eval):
        # Check if x coincides with a node
        diffs = x - nodes
        exact = np.where(np.abs(diffs) < 1e-15)[0]
        if len(exact) > 0:
            result[k] = fvals[exact[0]]
        else:
            terms = w / diffs
            result[k] = np.dot(terms, fvals) / np.sum(terms)

    return result


# --- Node distributions ---

def equidistant_nodes(N):
    return np.linspace(-1, 1, N + 1)


def cgl_nodes(N):
    """Chebyshev-Gauss-Lobatto nodes: x_j = cos(j*pi/N)."""
    return np.cos(np.arange(N + 1) * np.pi / N)


# --- Fine evaluation grid ---
x_fine = np.linspace(-1, 1, 1000)
f_fine = runge(x_fine)

# --- Polynomial degrees to show ---
degrees = [5, 10, 15]
colors = [ehplot.BLUE, ehplot.GOLD, ehplot.CRIMSON]

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(ehplot.TEXT_WIDTH, 2.3),
                                sharey=False)

# Panel (a): equidistant nodes
ax1.plot(x_fine, f_fine, "k-", linewidth=1.4, label=r"$f(x)$", zorder=5)

for N, c in zip(degrees, colors):
    nodes = equidistant_nodes(N)
    fvals = runge(nodes)
    p_fine = lagrange_interp(nodes, fvals, x_fine)
    ax1.plot(x_fine, p_fine, color=c, linewidth=0.9,
             label=rf"$N = {N}$", zorder=3)
    # Show nodes as small dots
    ax1.plot(nodes, fvals, "o", color=c, markersize=2.0, zorder=4)

ax1.set_xlabel(r"$x$")
ax1.set_ylabel(r"$p_N(x)$")
ax1.set_xlim(-1, 1)
ax1.set_ylim(-1.5, 2.0)
ax1.legend(loc="upper left", fontsize=6, ncol=2)
ax1.set_title(r"(a) Equidistant nodes", fontsize=8)

# Panel (b): Chebyshev-Gauss-Lobatto nodes
ax2.plot(x_fine, f_fine, "k-", linewidth=1.4, label=r"$f(x)$", zorder=5)

for N, c in zip(degrees, colors):
    nodes = cgl_nodes(N)
    fvals = runge(nodes)
    p_fine = lagrange_interp(nodes, fvals, x_fine)
    ax2.plot(x_fine, p_fine, color=c, linewidth=0.9,
             label=rf"$N = {N}$", zorder=3)
    # Show nodes as small dots
    ax2.plot(nodes, fvals, "o", color=c, markersize=2.0, zorder=4)

ax2.set_xlabel(r"$x$")
ax2.set_xlim(-1, 1)
ax2.set_ylim(-0.2, 1.15)
ax2.legend(loc="upper left", fontsize=6, ncol=2)
ax2.set_title(r"(b) Chebyshev nodes", fontsize=8)

fig.subplots_adjust(wspace=0.35)

# --- Save ---
out = Path(__file__).parent / "runge-phenomenon.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
