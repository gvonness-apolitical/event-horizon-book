"""Schwarzschild effective potential for null and timelike geodesics.

Generates figures/schw-effective-potential.pgf for inclusion in sec:schw-orbits.

Panel (a): Null geodesics — V_eff/L^2 vs r/M with photon sphere peak at r=3M.
Panel (b): Timelike geodesics — V_eff vs r/M for several L/M values, showing
           the stable/unstable circular orbit merger at the ISCO (r=6M).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np


# --- Effective potentials (M = 1) ---

def veff_null(r):
    """V_eff / L^2 for null geodesics: (1 - 2/r) / r^2."""
    return (1.0 - 2.0 / r) / r**2


def veff_timelike(r, L):
    """V_eff for timelike geodesics: (1 - 2/r)(1 + L^2/r^2)."""
    return (1.0 - 2.0 / r) * (1.0 + L**2 / r**2)


# --- Evaluation grids ---
r_null = np.linspace(2.01, 15, 500)
r_time = np.linspace(2.01, 25, 800)

# --- Timelike angular momenta ---
L_isco = 2.0 * np.sqrt(3.0)  # ~3.464
L_vals = [3.0, L_isco, 4.0, 5.0]
L_styles = [
    {"color": ehplot.GRAY, "linewidth": 1.0, "linestyle": "-",
     "label": r"$L/M = 3.0$"},
    {"color": ehplot.GOLD, "linewidth": 1.6, "linestyle": "-",
     "label": r"$L/M = 2\sqrt{3}$ (ISCO)"},
    {"color": ehplot.BLUE, "linewidth": 1.1, "linestyle": "-",
     "label": r"$L/M = 4.0$"},
    {"color": ehplot.CRIMSON, "linewidth": 1.1, "linestyle": "-",
     "label": r"$L/M = 5.0$"},
]


# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(ehplot.TEXT_WIDTH, 2.3))

# ---- Panel (a): null geodesics ----
V_null = veff_null(r_null)
ax1.plot(r_null, V_null, color=ehplot.GOLD, linewidth=1.4, zorder=3)

# Peak at r=3M: V_eff/L^2 = 1/27
r_peak = 3.0
V_peak = 1.0 / 27.0
ax1.plot(r_peak, V_peak, "o", color=ehplot.GOLD, markersize=4, zorder=5)

# Critical energy line (1/b_c^2)
ax1.axhline(V_peak, color=ehplot.GRAY, linewidth=0.5, linestyle=":",
            zorder=1)
ax1.text(13.5, V_peak + 0.0008, r"$1/b_c^2$",
         fontsize=7, color=ehplot.GRAY, ha="right", va="bottom")

# Horizon vertical
ax1.axvline(2.0, color=ehplot.CRIMSON, linewidth=0.7, linestyle="--",
            alpha=0.7, zorder=2)
ax1.text(2.15, 0.043, r"$r\!=\!2M$", fontsize=6, color=ehplot.CRIMSON,
         va="top")

# Photon sphere label
ax1.annotate(r"$r = 3M$", xy=(3.0, V_peak), xytext=(6.0, 0.043),
             fontsize=6, color=ehplot.GOLD,
             arrowprops=dict(arrowstyle="-|>", color=ehplot.GOLD,
                             lw=0.7),
             va="center")

ax1.set_xlabel(r"$r/M$")
ax1.set_ylabel(r"$V_{\mathrm{eff}}/L^2$")
ax1.set_xlim(1.8, 15)
ax1.set_ylim(-0.002, 0.050)
ax1.set_title(r"(a) Null geodesics", fontsize=8)

# ---- Panel (b): timelike geodesics ----
for L, style in zip(L_vals, L_styles):
    V = veff_timelike(r_time, L)
    ax2.plot(r_time, V, zorder=3, **style)

# E^2 = 1 reference (marginally bound)
ax2.axhline(1.0, color="k", linewidth=0.3, linestyle=":", zorder=1)
ax2.text(24.5, 1.003, r"$E^2\!=\!1$", fontsize=6, color=ehplot.GRAY,
         ha="right", va="bottom")

# Horizon vertical
ax2.axvline(2.0, color=ehplot.CRIMSON, linewidth=0.7, linestyle="--",
            alpha=0.7, zorder=2)
ax2.text(2.15, 1.055, r"$2M$", fontsize=6, color=ehplot.CRIMSON,
         va="top")

# ISCO vertical
ax2.axvline(6.0, color=ehplot.GOLD, linewidth=0.6, linestyle="--",
            alpha=0.5, zorder=2)
ax2.text(6.3, 1.055, r"ISCO", fontsize=6, color=ehplot.GOLD,
         va="top")

# ISCO inflection point marker
ax2.plot(6.0, 8.0 / 9.0, "o", color=ehplot.GOLD, markersize=3.5,
         zorder=5)

ax2.set_xlabel(r"$r/M$")
ax2.set_ylabel(r"$V_{\mathrm{eff}}$")
ax2.set_xlim(1.8, 25)
ax2.set_ylim(0.84, 1.06)
ax2.legend(loc="lower right", fontsize=5.5)
ax2.set_title(r"(b) Timelike geodesics", fontsize=8)

fig.subplots_adjust(wspace=0.40)

# --- Save ---
out = Path(__file__).parent / "schw-effective-potential.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
