"""Spectral vs finite-difference differentiation convergence.

Generates figures/diffmat-convergence.pgf for inclusion in sec:spec-diffmat.

Computes the supremum-norm error in the derivative of f(x) = exp(sin(pi*x))
on [-1,1] for:
  - Spectral differentiation matrix on CGL nodes (N = 2..40)
  - 2nd-order centred finite differences on equidistant grids
  - 4th-order centred finite differences on equidistant grids
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np


# --- Test function and exact derivative ---

def f(x):
    return np.exp(np.sin(np.pi * x))


def f_prime(x):
    return np.pi * np.cos(np.pi * x) * np.exp(np.sin(np.pi * x))


# --- Spectral differentiation matrix (CGL nodes) ---

def cgl_diffmat(N):
    """Build the (N+1)x(N+1) Chebyshev differentiation matrix on CGL nodes."""
    n = N + 1
    nodes = np.cos(np.pi * np.arange(N + 1) / N)

    # Endpoint flags
    c = np.ones(n)
    c[0] = 2.0
    c[N] = 2.0

    D = np.zeros((n, n))
    for i in range(n):
        row_sum = 0.0
        for j in range(n):
            if i != j:
                sign_ij = 1.0 if (i + j) % 2 == 0 else -1.0
                D[i, j] = (c[i] / c[j]) * sign_ij / (nodes[i] - nodes[j])
                row_sum += D[i, j]
        D[i, i] = -row_sum

    return nodes, D


# --- Spectral errors ---

N_spec = np.arange(2, 41)
spec_errors = np.empty(len(N_spec))

for idx, N in enumerate(N_spec):
    nodes, D = cgl_diffmat(N)
    fvals = f(nodes)
    fprime_numerical = D @ fvals
    fprime_exact = f_prime(nodes)
    spec_errors[idx] = np.max(np.abs(fprime_numerical - fprime_exact))

# Clamp to floor for log plot
spec_errors = np.maximum(spec_errors, 1e-16)


# --- Finite-difference errors ---

def fd2_error(N):
    """2nd-order centred FD on N+1 equidistant points in [-1,1]."""
    x = np.linspace(-1, 1, N + 1)
    h = x[1] - x[0]
    fvals = f(x)
    # Interior points only (centred stencil)
    fprime_fd = np.empty(N + 1)
    fprime_fd[0] = (fvals[1] - fvals[0]) / h  # one-sided
    fprime_fd[N] = (fvals[N] - fvals[N - 1]) / h  # one-sided
    for i in range(1, N):
        fprime_fd[i] = (fvals[i + 1] - fvals[i - 1]) / (2.0 * h)
    fprime_exact = f_prime(x)
    return np.max(np.abs(fprime_fd - fprime_exact))


def fd4_error(N):
    """4th-order centred FD on N+1 equidistant points in [-1,1]."""
    x = np.linspace(-1, 1, N + 1)
    h = x[1] - x[0]
    fvals = f(x)
    fprime_fd = np.empty(N + 1)
    fprime_exact = f_prime(x)
    for i in range(N + 1):
        if i < 2 or i > N - 2:
            # Fall back to 2nd-order at boundaries
            if i == 0:
                fprime_fd[i] = (fvals[1] - fvals[0]) / h
            elif i == N:
                fprime_fd[i] = (fvals[N] - fvals[N - 1]) / h
            else:
                im = max(i - 1, 0)
                ip = min(i + 1, N)
                fprime_fd[i] = (fvals[ip] - fvals[im]) / (2.0 * h)
        else:
            fprime_fd[i] = (-fvals[i + 2] + 8 * fvals[i + 1]
                            - 8 * fvals[i - 1] + fvals[i - 2]) / (12.0 * h)
    return np.max(np.abs(fprime_fd - fprime_exact))


N_fd = np.arange(4, 401)
fd2_errors = np.array([fd2_error(N) for N in N_fd])
fd4_errors = np.array([fd4_error(N) for N in N_fd])

# Clamp
fd2_errors = np.maximum(fd2_errors, 1e-16)
fd4_errors = np.maximum(fd4_errors, 1e-16)


# --- Plot ---

fig, ax = plt.subplots()

ax.semilogy(N_spec, spec_errors, color=ehplot.GOLD, linewidth=1.4,
            label="Spectral (CGL)", zorder=3)
ax.semilogy(N_fd, fd2_errors, color=ehplot.BLUE, linewidth=1.2,
            label=r"FD, $\mathcal{O}(h^2)$", zorder=2)
ax.semilogy(N_fd, fd4_errors, color=ehplot.GRAY, linewidth=1.2,
            linestyle="--",
            label=r"FD, $\mathcal{O}(h^4)$", zorder=2)

# Machine precision reference line
ax.axhline(y=np.finfo(float).eps, color=ehplot.GRAY, linewidth=0.5,
           linestyle=":", alpha=0.5, zorder=1)
ax.text(35, np.finfo(float).eps * 3, r"$\epsilon_{\mathrm{m}}$",
        fontsize=7, color=ehplot.GRAY, ha="right", va="bottom")

ax.set_xlabel(r"Number of points $N$")
ax.set_ylabel(r"$\|f_{\mathrm{numerical}}' - f_{\mathrm{exact}}'\|_\infty$")
ax.set_xlim(2, 400)
ax.set_ylim(1e-16, 1e2)

# Use log scale on y, linear on x but with log-like x range
ax.set_xscale("log")
ax.set_xlim(2, 400)

# Restore all four spines for log-scale axes
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)

ax.legend(loc="upper right", fontsize=7)

# --- Save ---
out = Path(__file__).parent / "diffmat-convergence.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
