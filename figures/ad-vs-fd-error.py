"""AD vs finite-difference accuracy for a Schwarzschild KS metric derivative.

Generates figures/ad-vs-fd-error.pgf for inclusion in sec:ad-comparison.

Computes the relative error in d_x g_tt at (t,x,y,z) = (0,5,0,0) for
M = 1 Schwarzschild in Kerr-Schild coordinates, sweeping the FD step
size h from 10^{-15} to 10^0.  The analytic derivative serves as the
reference value (equivalent to AD at machine precision).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


# --- Schwarzschild KS metric component g_tt and its x-derivative ---
#
# g_{tt} = -1 + 2M/r,  r = sqrt(x^2 + y^2 + z^2)
# d_x g_{tt} = d_x (2M/r) = -2M x / r^3

def g_tt(x, y, z, M=1.0):
    """Schwarzschild KS g_tt component."""
    r = np.sqrt(x**2 + y**2 + z**2)
    return -1.0 + 2.0 * M / r


def dg_tt_dx_exact(x, y, z, M=1.0):
    """Exact d_x g_tt for Schwarzschild KS."""
    r = np.sqrt(x**2 + y**2 + z**2)
    return -2.0 * M * x / r**3


# --- Parameters ---
M = 1.0
x0, y0, z0 = 5.0, 0.0, 0.0

exact = dg_tt_dx_exact(x0, y0, z0, M)

# --- FD sweep ---
h_vals = np.logspace(-15, 0, 500)
fd_errors = np.empty_like(h_vals)

for i, h in enumerate(h_vals):
    fd_approx = (g_tt(x0 + h, y0, z0, M) - g_tt(x0 - h, y0, z0, M)) / (2.0 * h)
    fd_errors[i] = abs(fd_approx - exact) / abs(exact)

# Clamp zeros (exact cancellation) to a small floor for log plot
fd_errors = np.maximum(fd_errors, 1e-18)

# --- AD reference error (machine precision) ---
# The analytic expression evaluates with ~1 ulp relative error.
# AD would give the same: exact propagation, rounded at each step.
ad_error = 2.0 * np.finfo(float).eps  # ~4.4e-16

# --- Guide lines ---
h_guide = np.logspace(-8, -0.5, 100)
# Truncation: E ~ h^2 (normalised to pass through the FD minimum region)
trunc_guide = 0.3 * (h_guide / 1e-5) ** 2 * 3.6e-11
# Round-off: E ~ 1/h
roundoff_guide = 3.6e-11 * (1e-5 / h_guide)

# --- Plot ---
fig, ax = plt.subplots()

ax.loglog(h_vals, fd_errors, color=ehplot.GOLD, linewidth=1.4,
          label="Central FD", zorder=3)
ax.axhline(y=ad_error, color=ehplot.BLUE, linestyle="--", linewidth=1.2,
           label="AD (forward-mode)", zorder=2)

# Guide lines (light grey, thin)
ax.loglog(h_guide, trunc_guide, color=ehplot.GRAY, linewidth=0.7,
          linestyle=":", alpha=0.6, zorder=1)
ax.loglog(h_guide, roundoff_guide, color=ehplot.GRAY, linewidth=0.7,
          linestyle=":", alpha=0.6, zorder=1)

# Guide-line labels
ax.text(3e-3, 1.5e-5, r"$\propto h^2$", fontsize=7, color=ehplot.GRAY,
        rotation=38, ha="left", va="bottom")
ax.text(2e-9, 1e-5, r"$\propto h^{-1}$", fontsize=7, color=ehplot.GRAY,
        rotation=-20, ha="left", va="bottom")

# Annotation: accuracy ceiling
ax.annotate(
    r"$\epsilon_{\mathrm{m}}^{2/3} \approx 10^{-11}$",
    xy=(6e-6, 3.6e-11), xytext=(3e-3, 3e-10),
    fontsize=7, color=ehplot.GOLD,
    arrowprops=dict(arrowstyle="->", color=ehplot.GOLD,
                    linewidth=0.8, shrinkA=0, shrinkB=3),
    ha="left", va="center",
)

# Annotation: AD level
ax.text(1e-13, ad_error * 3.5, r"$\sim\!\epsilon_{\mathrm{m}}$",
        fontsize=7, color=ehplot.BLUE, ha="left", va="bottom")

# Five orders of magnitude bracket (vertical double arrow)
bracket_x = 2e-1
ax.annotate(
    "", xy=(bracket_x, ad_error), xytext=(bracket_x, 3.6e-11),
    arrowprops=dict(arrowstyle="<->", color=ehplot.GRAY,
                    linewidth=0.8, shrinkA=2, shrinkB=2),
)
ax.text(bracket_x * 1.8, 2e-13, r"${\sim}\,10^5$", fontsize=7,
        color=ehplot.GRAY, ha="left", va="center")

ax.set_xlabel(r"FD step size $h$")
ax.set_ylabel(r"Relative error in $\partial_x g_{tt}$")
ax.set_xlim(1e-15, 1e0)
ax.set_ylim(1e-17, 1e0)

# Restore all four spines for log-log plot
ax.spines["top"].set_visible(True)
ax.spines["right"].set_visible(True)

ax.legend(loc="upper left", fontsize=7)

# --- Save ---
out = Path(__file__).parent / "ad-vs-fd-error.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
