.. _type6_ref:


Type 6
======

Type 6 is ladder nomograph:

.. math::
    u = u.

In practice this means that if one axis has for example y-position as

.. math::
    y = f_1(u)

and it was desirable to have

.. math::
    y = f_2(u)

in order to connect blocks together, one uses ladder to make the transformation.

.. note::
    Ladders are not beautiful and should be used only when no other solution exist.





Simple example
--------------
This simple example plots nomograph for equation:

.. math::
    u = u,

where linear scale is converted to a logarithmic scale.

Generated nomograph
^^^^^^^^^^^^^^^^^^^
.. image:: images/ex_type6_nomo_1.*
    :height: 600px

Source code of simple example of type6
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type6_nomo_1.py
        :encoding: latin-1
        :linenos:
        :lines: 1-4, 20-


Parameters for type 6
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 6
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

       "``'function'``", "--", "**func(u).** Function in equation For example ``lambda u: u``"
       "``'u_min'``", "--", "**Float.** Minimum value of function variable."
       "``'u_max'``", "--", "**Float.** Maximum value of function variable."

See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 6
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_6'``", "**String.** This is type 6 block."
    "``'type'``", "``'parallel'``", "**String.** Can be either ``'parallel'``or ``'orthogonal'``."
    "``'x_empty'``", "0.2", "**Float.** If orthogonal, how much fractional space before start of x-axis."
    "``'y_empty'``", "0.2", "**Float.** If orthogonal, how much fractional space before start of y-axis."
    "``'curve_const'``", "0.0", "**Float.** Sets the lenght of angle of Bezier curve. low value = straigh line, high value = curved line."
    "``'width'``", "10.0", "**Float.** Block width (to be scaled)"
    "``'height'``", "10.0", "**Float.** Block height (to be scaled)"
    "``'f1_params'``", "--", "**Axis params Dict.** Axis params for function f1"
    "``'f2_params'``", "--", "**Axis params Dict.** Axis params for function f2"
    "``'mirror_x'``", "``False``", "**Boolean.** If x-axis is mirrored"
    "``'mirror_y'``", "``False``", "**Boolean.** If y-axis is mirrored"
    "``'ladder_color'``", "``color.rgb.black``", "**Color.** Ladder color."
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Unknown values are given with strings, e.g. 'x'. An example:``[[0.8,'x'],[0.7,'x']]`` "


General parameters
^^^^^^^^^^^^^^^^^^

See :ref:`main_params` for top level main parameters.
