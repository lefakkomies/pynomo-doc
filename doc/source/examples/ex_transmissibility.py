# T=sqrt[(1+(2zr)**2)/((1-r**2)**2+(2zr)**2]
# Copyright Add LaMorille 2023
# merging of two type 5 blocks, as pynomo does not draw the whole function in one


from pynomo.nomographer import *
from pyx import *
import numpy as np

u_min = 0.1  # T
u_max = 6.0

wd_min_left = 0.05  # r
wd_max_left = 1.0

wd_min_right = 0.5  # r
wd_max_right = 10.0


def fT(r, z):  # u(x,v)
    r = np.exp(r)  # log x scale
    return ((1 + 4 * r * r * z * z) / (((1 - r * r) ** 2) + 4 * r * r * z * z)) ** 0.5


block_params_left = {
    'block_type': 'type_5',
    'u_func': lambda u: np.log10(u),  # log y scale
    'v_func': lambda x, v: np.log10(fT(x, v)),  # log y scale
    'u_values': [u_min, u_max],
    'scale_type_u': 'log smart',
    'u_tick_levels': 4,
    'u_tick_text_levels': 2,
    'u_title': '$T$',
    'u_title_draw_center': False,
    'u_tick_side': 'left',
    'v_values': [0.0, 0.2, 0.5, 1.0],
    'v_manual_axis_data': {0.0: r'', 0.2: r'', 0.5: r'', 1.0: r''},
    'v_title': '',
    'manual_x_scale': True,
    'scale_type_wd': 'log smart',
    'x_min': np.log(wd_min_left),  # log x scale
    'x_max': np.log(wd_max_left),  # log x scale
    'wd_func': lambda x: np.log(x),  # log x scale
    'wd_func_inv': lambda x: np.exp(x),  # log x scale
    'wd_tick_levels': 0,
    'wd_tick_text_levels': 0,
    'wd_title': '',
    'wd_tag': 'axis_left',
    'vertical_guides': False,
}

block_params_right = {
    'block_type': 'type_5',
    'u_func': lambda u: np.log10(u),
    'v_func': lambda x, v: np.log10(fT(x, v)),
    'u_values': [u_min, u_max],
    'scale_type_u': 'log smart',
    'u_tick_levels': 0,
    'u_tick_text_levels': 0,
    'u_title': '',
    'v_values': [0.0, 0.2, 0.5, 1.0],
    'v_manual_axis_data': {0.0: ['$\zeta=0.0$', {'x_corr': 2.25, 'y_corr': -14, 'draw_line': False}],
                           0.2: ['$\zeta=0.2$', {'x_corr': 4.5, 'y_corr': -9.5, 'draw_line': False}],
                           0.5: ['$\zeta=0.5$', {'x_corr': 5.75, 'y_corr': -6, 'draw_line': False}],
                           1.0: ['$\zeta=1.0$', {'x_corr': 6.9, 'y_corr': -3.75, 'draw_line': False}], },
    'v_title': '',
    'manual_x_scale': True,
    'scale_type_wd': 'log smart',
    'x_min': np.log(wd_min_right),
    'x_max': np.log(wd_max_right),
    'wd_func': lambda x: np.log(x),
    'wd_func_inv': lambda x: np.exp(x),
    'wd_tick_levels': 0,
    'wd_tick_text_levels': 0,
    'wd_title': '',
    'wd_tag': 'axis_right',
    'vertical_guides': False,
}

axis_params = {  # for proper axis management
    'tag': 'axis_left',
    'dtag': 'axis_right',
    'u_min': wd_min_left,
    'u_max': wd_max_right,
    'function': lambda u: np.log(u),
    'scale_type': 'log smart',
    'title': r'r',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_x_shift': 0.0,
    'title_y_shift': -1.2,
    'tick_side': 'left',
    'extra_params': [{'tick_side': 'left', 'scale_type': 'manual line',
                      'manual_axis_data': {1.414: r'$\sqrt 2$'}, }, ],
}

block_axis_params = {
    'block_type': 'type_8',
    'f_params': axis_params,
}


def post(c):  # hiding outlines
    c.stroke(path.line(8.515, 0.01, 8.515, 14.99) + path.line(6.565, 0.01, 6.565, 14.99),
             [style.linewidth.thick, color.cmyk.White])


main_params = {
    'filename': "ex_transmissibility.pdf",
    'paper_height': 15,
    'paper_width': 15,
    'block_params': [block_params_left, block_params_right, block_axis_params],
    'transformations': [('scale paper',)],
    'make_grid': False,
    'draw_lines': True,
    'line_params': [{'coords': [[0, 8.435, 9.49, 8.435], [9.495, 8.435, 9.495, 0]],  # manual isopleth
                     'line_style': [color.cmyk.Black, style.linewidth.thick, style.linestyle.dashed],
                     'circle_size': 0.0, }],
    'title_x': 12.75,
    'title_y': 14.0,
    'title_box_width': 4.0,
    'title_str': r'\large Pynomo Type 5 \par \
                   \par $T=\sqrt{{1+(2 \zeta r)^2}\over{(1-r^2)^2+(2 \zeta r)^2}}$ \par \
                   \par \normalsize $T=$ transmissibility \par $\zeta=$ damping ratio \par $r=$ frequency ratio',
    'post_func': post,
}

Nomographer(main_params)
