"""
    tutorial1b.py

    Simple nomogram of relationship between auto fuel consumption and distance travelled

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
    # fuel efficiency in litres / 100 kilometres) (u2)
    'u_min': 5.0,
    'u_max': 20.0,
    'function': lambda u: 100.0/u,
    'title': r'litres per 100 kms',
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
    'filename': 'tutorial1b.eps',
    'paper_height':15.0,
    'paper_width':15.0,
    'block_params': [block_SI],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\LARGE Fuel economy calculator (Variation)',
    # 'make_grid': True,
}
Nomographer(main_params)
