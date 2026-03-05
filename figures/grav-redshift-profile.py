"""Gravitational redshift z(r) for a Schwarzschild black hole.

Generates figures/grav-redshift-profile.pgf for inclusion in
sec:gr-weak-field.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ehplot

import matplotlib.pyplot as plt
import numpy as np

# --- Data ---
r = np.linspace(2.01, 30.0, 1000)  # r/M

z_exact = 1.0 / np.sqrt(1.0 - 2.0 / r) - 1.0
z_weak = 1.0 / r  # weak-field: z ≈ M/r

# --- Plot ---
fig, ax = plt.subplots()

ax.plot(r, z_exact, color=ehplot.BLUE, label=r"$z = (1-2M/r)^{-1/2} - 1$")
ax.plot(r, z_weak, color=ehplot.GRAY, linestyle="--",
        label=r"$z \approx M/r$ (weak field)")

# Vertical markers at key radii
ax.axvline(x=6.0, color=ehplot.BLUE, linestyle=":", linewidth=0.8,
           alpha=0.7)
ax.axvline(x=3.0, color=ehplot.GOLD, linestyle=":", linewidth=0.8,
           alpha=0.7)
ax.axvline(x=2.0, color=ehplot.CRIMSON, linestyle=":", linewidth=0.8,
           alpha=0.7)

# Labels for vertical lines
# r=2M: right-aligned, tucked between y=3 and y=4
ax.text(1.8, 3.7, r"$r\!=\!2M$", fontsize=7, color=ehplot.CRIMSON,
        ha="right", va="bottom")
ax.text(1.8, 3.6, "horizon", fontsize=6, color=ehplot.CRIMSON,
        ha="right", va="top", style="italic")

# r=3M: right-aligned, below the r=2M block
ax.text(3.2, 2.9, r"$r\!=\!3M$", fontsize=7, color=ehplot.GOLD,
        ha="left", va="bottom")
ax.text(3.2, 2.8, "photon\nsphere", fontsize=6, color=ehplot.GOLD,
        ha="left", va="top", style="italic", linespacing=0.9)

# r=6M: left-aligned, just right of the dotted line
ax.text(6.2, 3.7, r"$r\!=\!6M$", fontsize=7, color=ehplot.BLUE,
        ha="left", va="bottom")
ax.text(6.2, 3.6, "ISCO", fontsize=6, color=ehplot.BLUE,
        ha="left", va="top", style="italic")

ax.set_xlabel(r"$r / M$")
ax.set_ylabel(r"Redshift $z$")
ax.set_xlim(2.0, 30.0)
ax.set_ylim(0.0, 4.5)
ax.legend(loc="upper right", fontsize=7)

# --- Save ---
out = Path(__file__).parent / "grav-redshift-profile.pgf"
fig.savefig(str(out))
plt.close(fig)
print(f"Wrote {out}")
