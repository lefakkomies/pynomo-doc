"""
    tutorial1a.py

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

dist_SI = {
    # distance in kilometers (u1)
    'u_min': 100.0,
    'u_max': 1000.0,
    'function': lambda u: u,
    'title': r'kms',
    'tick_levels': 3,
    'tick_text_levels': 2,
}

eff_SI = {
    # fuel efficiency in km / litre) (u2)
    'u_min': 5.0,
    'u_max': 20.0,
    'function': lambda u: u,
    'title': r'kms per litre',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
}

fuel_SI = {
    # fuel consumption in litres (u3)
    'u_min': 10.0,
    'u_max': 100.0,
    'function': lambda u: u,
    'title': r'litres',
    'tick_levels': 3,
    'tick_text_levels': 2,
}

block_SI = {
    'block_type': 'type_2',
    'f1_params': dist_SI,
    'f2_params': eff_SI,
    'f3_params': fuel_SI,
}

main_params = {
    'filename': 'tutorial1a.eps',
    'paper_height':15.0,
    'paper_width':15.0,
    'block_params': [block_SI],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\LARGE Fuel economy calculator',
}
Nomographer(main_params)
