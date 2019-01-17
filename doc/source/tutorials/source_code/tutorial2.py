"""
    tutorial2.py

    Simple nomogram of relationship between auto fuel consumption and distance travelled

    Copyright (C) 2018  Daniel Boulet

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
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *

text.set(mode="latex")  # allows use of latex commands in PyX such as \frac{a}{b} and \par

dist_SI = {
    # distance in kilometers (u1)
    'tag': 'distance',
    'u_min': 100.0,
    'u_max': 1000.0,
    'function': lambda u: u,
    'title': r'$km$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_x_shift': 1.0,
}

dist_US = {
    # distance in miles (u1)
    'tag': 'distance',
    'u_min': 100.0/1.609344,    # convert kilometers to miles
    'u_max': 1000.0/1.609344,
    'function': lambda u: u,    # plot the u values linearly ...
    'align_func': lambda u: u*1.609344,   # but adjust the length to match kilometers
    'title': r'$mi.$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'tick_side': 'left',
    'title_x_shift': -1.0,
}

eff_SI = {
    # fuel efficiency in km / litre) (u2)
    'u_min': 5.0,
    'u_max': 20.0,
    'function': lambda u: 100.0/u,
    'title': r'$\frac{L}{100 \, km}$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
    'title_draw_center': True,
    'title_distance_center': -2.0,
}

eff_US = {
    # fuel efficiency in miles per US gallon) u2
    'u_min': 235.189/20.0,      # magic value to coordinate length of SI and US scale
    'u_max': 235.189/5.0,
    'function': lambda u: u,
    'title': r'$\frac{mi.}{US \, gal.}$',
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'title_draw_center': True,
    'title_distance_center': -1.5,
}

fuel_SI = {
    # fuel consumption in litres (u3)
    'tag': 'consumption',
    'u_min': 10.0,
    'u_max': 100.0,
    'function': lambda u: u,
    'title': r'$L$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_x_shift': 1.0,
}

fuel_US = {
    # fuel consumption in US gallons
    'tag': 'consumption',
    'u_min': 10.0/3.785,    # convert liters to USG
    'u_max': 100.0/3.785,
    'function': lambda u: u,    # plot the gallons
    'align_func': lambda u: u*3.785,   # but must be scaled up to litres
    'title': r'$US \, gal.$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'tick_side': 'left',
    'title_x_shift': -1.0,
}

block_SI = {
    'block_type': 'type_2',
    'f1_params': dist_SI,
    'f2_params': eff_SI,
    'f3_params': fuel_SI,
    'isopleth_values': [[600, 'x', 90]],
}

block_US = {
    'block_type': 'type_2',
    'f1_params': dist_US,
    'f2_params': eff_US,
    'f3_params': fuel_US,
    'isopleth_values': [[550, 40.0, 'x']],
}

main_params = {
    'filename': 'tutorial2.pdf',
    'paper_height':15.0,
    'paper_width':15.0,
    'block_params': [block_SI, block_US],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\LARGE Fuel economy calculator (Metric and US)',
}
Nomographer(main_params)
