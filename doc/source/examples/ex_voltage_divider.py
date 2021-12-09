"""
    ex_voltage_divider.py

    Nomogram to calculate resistor values for simple voltage divider.  This
    nomogram uses grid rather than matrix.

    Copyright (C) 2018-2021 Daniel Boulet

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

from pynomo.nomographer import *
import sys
sys.path.insert(0, "..")

from pyx import *
pyx.text.set(text.LatexEngine)

resistors = [
	1.0,	1.1,	1.2,
	1.3,	1.5,	1.6,
	1.8,	2.0,	2.2,
	2.4,	2.7,	3.0,
	3.3,	3.6,	3.9,
	4.3,	4.7,	5.1,
	5.6,	6.2,	6.8,
	7.5,	8.2,	9.1
]

# Type 5 contour
def f1(x, u):
    return u*(1-x)/x


block_1_params = {
    'width': 12.0,
    'height': 25.0,
    'block_type': 'type_5',

    'u_func': lambda u: u,
    'u_values': resistors,
    'u_axis_color': pyx.color.cmyk.Red,
    'u_title': r'\Large{$R_a$}',
    'u_text_format': r"\normalsize{$%3.1f$}",

    'v_func': f1,
    'v_values': resistors,
    'v_axis_color': pyx.color.cmyk.Red,
    'v_title': r'\Large{$R_b$}',
    'v_text_format': r"\normalsize{$%3.1f$}",

    'wd_tag': 'A',
    'wd_tick_side': 'right',
    'wd_axis_color': pyx.color.cmyk.Gray,
    'isopleth_values': [
        [6.2, 'x', 'x'],
    ],
    'vertical_guide_nr': 10

}

# this is non-obvious trick to find bottom edge coordinates of the grid in order
# to align it with N nomogram
block1_dummy = Nomo_Block_Type_5(mirror_x=False)
block1_dummy.define_block(block_1_params)
block1_dummy.set_block()

# Let's define the N-nomogram
N_params_3 = {
    'u_min': block1_dummy.grid_box.params_wd['u_min'],
    'u_max': block1_dummy.grid_box.params_wd['u_max'],
    'function': lambda u: u,
    'title': '',
    'tag': 'A',
    'tick_side': 'right',
    'tick_levels': 2,
    'tick_text_levels': 2,
    'reference': False,
    'tick_levels': 0,
    'tick_text_levels': 0,
    'title_draw_center': True
}
N_params_2 = {
    'u_min': 6.0,
    'u_max': 24.0,
    'function': lambda u: u,
    'title': r'$V_{in}$',
    'tag': 'none',
    'tick_side': 'left',
    'tick_levels': 4,
    'tick_text_levels': 3,
    'title_draw_center': True,
    'scale_type': 'linear smart',
}
N_params_1 = {
    'u_min': 1.0,
    'u_max': 10.0,
    'function': lambda u: u,
    'title': r'$V_{out}$',
    'tag': 'none',
    'scale_type': 'linear smart',
    'tick_side': 'right',
    'tick_levels': 3,
    'tick_text_levels': 3,
    'title_draw_center': True
}

block_2_params = {
    'block_type': 'type_2',
    'f1_params': N_params_1,
    'f2_params': N_params_2,
    'f3_params': N_params_3,
    'isopleth_values': [
        # Vout, Vin, ratio
        [3.3, 9.0, 'x'],
    ]
}

main_params = {
    'filename': 'ex_voltage_divider.pdf',
    'paper_height': 8.5*2.54,
    'paper_width': 11.0*2.54,
    'block_params': [block_1_params, block_2_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\Large Voltage Divider Nomograph \par \
        \normalsize (For E24 series values) \par \bigskip \
        \large $V_{out}=V_{in} \cdot \frac{R_b}{R_a+R_b}$ \
        \par \bigskip   \normalsize \copyright    Daniel Boulet  2018-2021',
    'title_x': 2.0,
    'title_y': 6.0,
    'isopleth_params': [
        {
            'color': 'blue',
            'linewidth': 'thick',
            'linestyle': 'dashed',
            'circle_size': 0.10,
        },
    ],
}

Nomographer(main_params)
