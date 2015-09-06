

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: General params
    :class: longtable
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 40

    "``'filename'``", "``'pynomo_default.pdf'``", "**String.** Filename of generated file. .pdf and .eps formats supported."
    "``'paper_height'``", "``20.0``", "**String.** Height of paper (roughly, ticks and texts extend this)."
    "``'paper_width'``", "``20.0``", "**String.** Width of paper (roughly, ticks and texts extend this)."
    "``'block_params'``", " ", "**Array of Blocks.** List of blocks that make the nomograph."
    "``'transformations'``", "``[('rotate', 0.01), ('scale paper')]``", "**Array of tuples.** List of transformations to transform nomograph."
    "``'title_str'``", "``''``", "**String.** Title string of nomograph."
    "``'title_x'``", "paper_width/2.0", "**Float.** Title x-position."
    "``'title_y'``", "paper_height", "**Float.** Title y-position."
    "``'title_box_width'``", "paper_width/2.2", "**Float.** Title box width."
    "``'title_color'``", "``'color.rgb.black'``", "**Color.** Title color."
    "``'make_grid'``", "``False``", "**Boolean.** If True, draws grid to help position texts, etc."
    "``'pre_func'``", "``None``", "**func(context).** PyX function(canvas) to draw under nomograph. Function definition could be:

    .. literalinclude:: snippets/pre_func_ex.py "
    "``'post_func'``", "``None``", "**func(context).** PyX function(canvas) to draw over nomograph. Definiton same as for 'pre_func'."
    "``'debug'``", "``False``", "**Boolean.** If True, prints dicts of definions."
    "``'extra_texts'``", "``[]``", "**List of Dicts defining texts.** Defines extra texts. Could be for example:

    .. literalinclude:: snippets/extra_texts_ex.py "
    "``'isopleth_params'``", "``[{}]``", "**List of Dicts.** Defines appearance of isopleths. Could be for example:

    .. literalinclude:: snippets/isopleth_params_ex.py "




