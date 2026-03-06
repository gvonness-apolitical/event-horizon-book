"""Kerr ISCO radius and radiative efficiency vs dimensionless spin.

Generates figures/kerr-isco.pgf for inclusion in sec:kerr-isco.

Two y-axes:
  Left:  r_ISCO / M  (prograde and retrograde)
  Right: radiative efficiency eta (prograde only)
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np

# --- Bardeen-Press-Teukolsky ISCO formulae ---

def kerr_isco(a_star, prograde=True):
    """ISCO radius in units of M, from Bardeen et al. (1972)."""
    a2 = a_star ** 2
    Z1 = 1.0 + (1.0 - a2) ** (1.0 / 3.0) * (
        (1.0 + a_star) ** (1.0 / 3.0) + (1.0 - a_star) ** (1.0 / 3.0)
    )
    Z2 = np.sqrt(3.0 * a2 + Z1 ** 2)
    inner = np.sqrt((3.0 - Z1) * (3.0 + Z1 + 2.0 * Z2))
    if prograde:
        return 3.0 + Z2 - inner
    else:
        return 3.0 + Z2 + inner


def kerr_circ_energy(r, a_star, prograde=True):
    """Specific energy for circular equatorial orbit at r/M."""
    # Upper sign (+) = prograde
    sign = 1.0 if prograde else -1.0
    r32 = r ** 1.5
    r12 = np.sqrt(r)
    r34 = r ** 0.75
    num = r32 - 2.0 * r12 + sign * a_star
    den = r34 * np.sqrt(np.abs(r32 - 3.0 * r12 + sign * 2.0 * a_star))
    return num / den


# --- Data ---
a = np.linspace(0.0, 0.9999, 2000)

r_pro = np.array([kerr_isco(ai, prograde=True) for ai in a])
r_retro = np.array([kerr_isco(ai, prograde=False) for ai in a])

# Radiative efficiency: eta = 1 - E_ISCO
eta = np.array([
    1.0 - kerr_circ_energy(kerr_isco(ai, True), ai, True)
    for ai in a
])

# --- Plot ---
fig, ax1 = plt.subplots()

# Left axis: ISCO radius
ax1.plot(a, r_pro, color=ehplot.GOLD, linestyle="-",
         label=r"$r_{\mathrm{ISCO}}^{\mathrm{pro}}$")
ax1.plot(a, r_retro, color=ehplot.BLUE, linestyle="--",
         label=r"$r_{\mathrm{ISCO}}^{\mathrm{retro}}$")

ax1.set_xlabel(r"$a/M$")
ax1.set_ylabel(r"$r_{\mathrm{ISCO}} / M$")
ax1.set_xlim(0.0, 1.0)
ax1.set_ylim(0.5, 9.5)

# Horizontal reference lines
ax1.axhline(y=6.0, color=ehplot.GRAY, linestyle=":", linewidth=0.6,
            alpha=0.5)
ax1.axhline(y=1.0, color=ehplot.GRAY, linestyle=":", linewidth=0.6,
            alpha=0.5)
ax1.axhline(y=9.0, color=ehplot.GRAY, linestyle=":", linewidth=0.6,
            alpha=0.5)

# Vertical reference at a/M = 0.9
ax1.axvline(x=0.9, color=ehplot.GRAY, linestyle=":", linewidth=0.6,
            alpha=0.5)

# Markers at a/M = 0.9
r_pro_09 = kerr_isco(0.9, True)
r_retro_09 = kerr_isco(0.9, False)
ax1.plot(0.9, r_pro_09, "o", color=ehplot.GOLD, markersize=3.5,
         zorder=5)
ax1.plot(0.9, r_retro_09, "o", color=ehplot.BLUE, markersize=3.5,
         zorder=5)

# Annotations for the a=0.9 markers
ax1.annotate(
    rf"$\approx {r_pro_09:.1f}M$",
    xy=(0.9, r_pro_09), xytext=(0.72, r_pro_09 + 1.5),
    fontsize=6.5, color=ehplot.GOLD,
    arrowprops=dict(arrowstyle="-", color=ehplot.GOLD, lw=0.5),
    ha="center",
)
ax1.annotate(
    rf"$\approx {r_retro_09:.1f}M$",
    xy=(0.9, r_retro_09), xytext=(0.72, r_retro_09 - 1.3),
    fontsize=6.5, color=ehplot.BLUE,
    arrowprops=dict(arrowstyle="-", color=ehplot.BLUE, lw=0.5),
    ha="center",
)

# Schwarzschild label
ax1.text(0.02, 6.2, r"$6M$ (Schwarzschild)", fontsize=6.5,
         color=ehplot.GRAY, va="bottom")

ax1.legend(loc="center left", fontsize=7)

# Right axis: radiative efficiency
ax2 = ax1.twinx()
ax2.plot(a, eta * 100, color=ehplot.CRIMSON, linestyle="-.",
         linewidth=0.9, label=r"$\eta$ (prograde)")
ax2.set_ylabel(r"Efficiency $\eta$ (\%)")
ax2.set_ylim(0, 48)

# Ensure right spine is visible for the twin axis
ax2.spines["right"].set_visible(True)

# Efficiency reference lines
ax2.axhline(y=5.7, color=ehplot.CRIMSON, linestyle=":", linewidth=0.5,
            alpha=0.4)
ax2.axhline(y=42.3, color=ehplot.CRIMSON, linestyle=":", linewidth=0.5,
            alpha=0.4)

ax2.text(0.02, 7.0, r"$5.7\%$", fontsize=6, color=ehplot.CRIMSON,
         alpha=0.7, va="bottom")
ax2.text(0.02, 43.5, r"$42.3\%$", fontsize=6, color=ehplot.CRIMSON,
         alpha=0.7, va="bottom")

ax2.legend(loc="upper left", fontsize=7, bbox_to_anchor=(0.0, 0.85))

# --- Save ---
out = Path(__file__).parent / "kerr-isco.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
