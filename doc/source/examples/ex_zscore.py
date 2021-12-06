"""
    ex_zscore.py

    Nomograph to calculate area under normal curve from z-score.

    Copyright (C) 2019      Daniel Boulet

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import scipy.stats as stats
from pynomo.nomographer import *
import sys

sys.path.insert(0, "..")
# allows use of latex commands in PyX such as \frac{a}{b} and \par
from pyx import *

pyx.text.set(text.LatexEngine)


def cdf(u):
    return stats.norm.cdf(u)


def ppf(u):
    return stats.norm.ppf(u)


lmin = 0.0001
lmax = 0.9999

sd1 = cdf(1.0) - cdf(-1.0)
sd2 = cdf(2.0) - cdf(-2.0)
sd3 = cdf(3.0) - cdf(-3.0)


leftpdf = {
    "tag": "a",
    "u_min": lmin,
    "u_max": 0.5,
    "function": lambda u: (u),
    "scale_type": "manual point",
    # extra parameters
    "extra_params": [
        {
            "scale_type": "manual arrow",
            "manual_axis_data": {
                cdf(-1.0): r"%4.4f" % cdf(-1.0),
                cdf(-2.0): r"%4.4f" % cdf(-2.0),
                cdf(-3.0): r"%4.4f" % cdf(-3.0),
                cdf(-1.25): r"%4.4f" % cdf(-1.25),
            },
            "arrow_length": 2.0,
        },
    ],
}


leftz = {
    "tag": "a",
    "u_min": ppf(lmin),
    "u_max": ppf(0.5),
    "function": lambda u: cdf(u),
    "align_func": lambda u: cdf(u),
    "title": "Lower tail $X_1$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
    "tick_side": "left",
}


rightpdf = {
    "tag": "c",
    "u_min": 0.5,
    "u_max": lmax,
    "function": lambda u: -(u),
    "scale_type": "manual point",
    # extra parameters
    "extra_params": [
        {
            "scale_type": "manual arrow",
            "tick_side": "left",
            "manual_axis_data": {
                cdf(3.0): r"%4.4f" % cdf(3.0),
                cdf(2.0): r"%4.4f" % cdf(2.0),
                cdf(1.0): r"%4.4f" % cdf(1.0),
                cdf(0.25): r"%4.4f" % cdf(0.25),
            },
            "arrow_length": 2.0,
        },
    ],
}


rightz = {
    "tag": "c",
    "u_min": ppf(0.5),
    "u_max": ppf(lmax),
    "function": lambda u: cdf(u),
    "align_func": lambda u: cdf(u),
    "title": "Upper tail $X_2$",
    # 'title_x_shift': 2.0,
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

leftblock2 = {"block_type": "type_8", "f_params": leftz, "isopleth_values": [["x"]]}


rightblock2 = {"block_type": "type_8", "f_params": rightz, "isopleth_values": [["x"]]}


delta = {
    "u_min": 0.0,
    "u_max": 1.0,
    "function": lambda u: u,
    "scale_type": "linear smart",
    "title": "Area",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "extra_params": [
        {
            "tick_side": "left",
            "scale_type": "manual arrow",
            "manual_axis_data": {
                sd1: r"$\pm 1 \sigma$ %4.4f" % sd1,
                sd2: r"$\pm 2 \sigma$ %4.4f" % sd2,
                sd3: r"$\pm 3 \sigma$ %4.4f" % sd3,
            },
            "arrow_length": 2.0,
        },
    ],
}

block_diff = {
    "block_type": "type_1",
    "f1_params": leftpdf,
    "f2_params": delta,
    "f3_params": rightpdf,
    "proportion": 1.5,
    # 'width':15.0,
    # 'height':15.0,
    "isopleth_values": [[cdf(-1.25), "x", cdf(0.25)]],
}


main_params = {
    "filename": "example_zscore.pdf",
    "paper_height": 11.0 * 2.54,
    "paper_width": 8.5 * 2.54,
    "block_params": [block_diff, leftblock2, rightblock2],
    "cdfations": [("rotate", 0.01), ("scale paper",), ("polygon",)],
    "title_x": 6.50,
    "title_y": 27.0,
    "title_box_width": 7.0,
    "title_str": r"\Huge $Z$-scores Nomograph \par \medskip \large ($\mu = 0$, $\sigma = 1$)",
    # 'make_grid':True,
    "extra_texts": [
        {
            "x": 4.5,
            "y": 4.5,
            "text": r"\noindent Area under normal curve between lower tail $X_1$ and upper tail $X_2$ is read on center axis. \
                For example, area under normal distribution curve from $%g \sigma$ to $%g \sigma$ is $%4.4f$."
            % (-1.25, 0.25, cdf(0.25) - cdf(-1.25)),
            "width": 10.0,
        },
        {
            "x": 15.0,
            "y": 1.0,
            "text": r"\copyright Daniel Boulet  2019",
            "width": 10.0,
        },
    ],
}

Nomographer(main_params)
