.. _type8_ref:

Type 8
======

Type 8 is single nomograph:

.. math::
    y = F(u)

or

.. math::
    x = F_x(u),

.. math::
    y = F_y(u).

x and y are coordinates of canvas.
Often this block is used for construction of dual-scales to
existing scales.



Simple example
--------------
This simple example plots single vertical scale.



Generated nomograph
^^^^^^^^^^^^^^^^^^^
.. image:: images/ex_type8_nomo_1.*
    :height: 600px

Source code of simple example of type 8
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type8_nomo_1.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-


Parameters for type 8
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 8
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

       "``'function'``", "--", "**func(u).** Function in equation. For example ``lambda u: u``."
       "``'u_min'``", "--", "**Float.** Minimum value of function variable."
       "``'u_max'``", "--", "**Float.** Maximum value of function variable."
       "``'function_x'``", "--", "**func(u).** x-position in function. If used 'function_y' must be defined. For example ``lambda u: u``."
       "``'function_y'``", "--", "**func(u).** y-position in function. If used 'function_x' must be defined. Overrides 'function'. For example ``lambda u: u``."

See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 8
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_8'``", "**String.** This is type 8 block"
    "``'width'``", "10.0", "**Float.** Block width (to be scaled)"
    "``'height'``", "10.0", "**Float.** Block height (to be scaled)"
    "``'f1_params'``", "--", "**Axis params Dict.** Axis params for function f1"
    "``'f2_params'``", "--", "**Axis params Dict.** Axis params for function f2"
    "``'f3_params'``", "--", "**Axis params Dict.** Axis params for function f3"
    "``'f4_params'``", "--", "**Axis params Dict.** Axis params for function f4"
    "``'mirror_x'``", "``False``", "**Boolean.** If x-axis is mirrored"
    "``'mirror_y'``", "``False``", "**Boolean.** If y-axis is mirrored"
    "``'padding'``", "``0.9``", "**Float.** How much axis extend w.r.t. width/height."
    "``'float_axis'``", "``'F1 or F2'``", "**Strings.** If given 'F1 or F2', then scaling is according to them, otherwise according to F3 and F4."
    "``'reference_color'``", "``color.rgb.black``", "**Color.** Color of reference lines."
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Unknown values are given with strings, e.g. 'x'. An example:``[[0.8,'x',0.7,0.5], [0.7,0.8,'x',0.3]]`` "


General parameters
^^^^^^^^^^^^^^^^^^

See :ref:`main_params` for top level main parameters.
