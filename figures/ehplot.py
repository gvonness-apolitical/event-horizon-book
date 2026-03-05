"""ehplot — Matplotlib pgf preamble for Event Horizon book figures.

Import this module before creating figures to configure the pgf backend
with fontspec font loading that matches ehbook.cls exactly.

Usage:
    import ehplot  # sets pgf preamble
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ...
    fig.savefig('figures/my_figure.pgf')
"""

import matplotlib
matplotlib.use("pgf")
import matplotlib.pyplot as plt
from pathlib import Path

# Load the companion style file
_style_path = Path(__file__).parent / "ehbook.mplstyle"
plt.style.use(str(_style_path))

# Use LuaLaTeX (matches ehbook.cls; XeTeX default can't find all fonts)
matplotlib.rcParams["pgf.texsystem"] = "lualatex"

# pgf preamble: load fonts via fontspec to match ehbook.cls
matplotlib.rcParams["pgf.preamble"] = "\n".join([
    r"\usepackage{fontspec}",
    r"\usepackage{unicode-math}",
    r"\setmainfont{STIX Two Text}[Numbers=OldStyle, Ligatures=TeX]",
    r"\setmathfont{STIX Two Math}",
    r"\setmonofont{Source Code Pro}[Scale=MatchLowercase]",
])

# Accretion Disk palette as named constants for direct use
GOLD = "#C48E36"
BLUE = "#406699"
CRIMSON = "#9E302C"
GRAY = "#6E6C76"

PALETTE = [GOLD, BLUE, CRIMSON, GRAY]

# Standard figure widths (inches) matching ehbook.cls page layout
TEXT_WIDTH = 4.094   # 104mm
MARGIN_WIDTH = 1.654  # 42mm
