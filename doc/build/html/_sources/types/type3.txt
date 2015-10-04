.. _type3_ref:

Type 3
======

Type 3 has N parallel lines that have functional relationship:

.. math::
    F_1(u_1) + F_2(u_2) + \cdots + F_N(u_N) = 0

Use of this nomograph is given by the following
simple example.

Simple example
--------------
This simple example plots nomograph for equation:

.. math::
    u_1 + u_2 + u_3 + u_4 + u_5 + u_6 = 0


Generated nomograph
^^^^^^^^^^^^^^^^^^^
.. image:: images/ex_type3_nomo_1.*

Source code of simple example of type 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type3_nomo_1.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-


Parameters for type 3
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 3
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

       "``'function'``", "--", "**func(u).** Function in equation For example ``lambda u: u``"
       "``'u_min'``", "--", "**Float.** Minimum value of function variable."
       "``'u_max'``", "--", "**Float.** Maximum value of function variable."

See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 3
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_3'``", "**String.** This is type 3 block"
    "``'width'``", "10.0", "**Float.** Block width (to be scaled)"
    "``'height'``", "10.0", "**Float.** Block height (to be scaled)"
    "``'f_params'``", "--", "**List of Axis params Dict.** List of Axis params."
    "``'mirror_x'``", "``False``", "**Boolean.** If x-axis is mirrored"
    "``'mirror_y'``", "``False``", "**Boolean.** If y-axis is mirrored"
    "``'reference_padding'``", "``0.2``", "**Float.** Additional length to reference axes."
    "``'reference_titles'``", "``[]``", "**Array of Strings.** List of reference line titles. For example `['$R_1$','$R_2$','$R_3$']``."
    "``'reference_color'``", "``color.rgb.black``", "**Color.** Color of reference lines."
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Unknown values are given with strings, e.g. 'x'. An example:``[[0.8,'x',0.7,7.0,9.0],[0.7,0.8,'x',5.0,4.44]]`` "


General parameters
^^^^^^^^^^^^^^^^^^

See :ref:`main_params` for top level main parameters.
