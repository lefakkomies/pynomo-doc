.. _type4_ref:

Type 4
======

Type 4 is proportion nomograph that have functional relationship:

.. math::
    \frac{F_1(u_1)}{F_2(u_2)} = \frac{F_3(u_3)}{F_4(u_4)}


Simple example
--------------
This simple example plots nomograph for equation:

.. math::
    u_1 / u_2 = u_3 / u_4


Generated nomograph
^^^^^^^^^^^^^^^^^^^
.. image:: images/ex_type4_nomo_1.*

Source code of simple example of type 4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type4_nomo_1.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-


Parameters for type 4
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 4
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

       "``'function'``", "--", "**func(u).** Function in equation For example ``lambda u: u``"
       "``'u_min'``", "--", "**Float.** Minimum value of function variable."
       "``'u_max'``", "--", "**Float.** Maximum value of function variable."

.. only:: html

    .. include:: axis_params.rst

.. only:: latex

    See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 4
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_4'``", "**String.** This is type 4 block"
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
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Unknown values are given with strings, e.g. 'x'. An example:``[[0.8,'x',0.7,0.5],[0.7,0.8,'x',0.3]]`` "


General parameters
^^^^^^^^^^^^^^^^^^
.. only:: html

    .. include:: general_params.rst

.. only:: latex

    See :ref:`main_params` for top level main parameters.
