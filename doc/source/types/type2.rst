.. _type2_ref:

Type 2
======

Type 1 is "N" or "Z" nomograph that have functional relationship:

.. math::
    F_1(u_1) = F_2(u_2) F_3(u_3)

Use of this nomograph is given by the following
simple example.

Simple example
--------------
This simple example plots nomograph for equation:

.. math::
    u_1 = u_2 u_3


Generated nomograph
^^^^^^^^^^^^^^^^^^^
.. image:: images/ex_type2_nomo_1.*

Source code of simple example of type 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type2_nomo_1.py
        :encoding: latin-1
        :linenos:
        :lines: 1-4, 20-


Parameters for type 2
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 2
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

       "``'function'``", "--", "**func(u).** Function in equation For example ``lambda u: u``"
       "``'u_min'``", "--", "**Float.** Minimum value of function variable."
       "``'u_max'``", "--", "**Float.** Maximum value of function variable."

See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 2
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_2'``", "**String.** This is type 2 block"
    "``'width'``", "10.0", "**Float.** Block width (to be scaled)"
    "``'height'``", "10.0", "**Float.** Block height (to be scaled)"
    "``'f1_params'``", "--", "**Axis params Dict.** Axis params for function f1"
    "``'f2_params'``", "--", "**Axis params Dict.** Axis params for function f2"
    "``'f3_params'``", "--", "**Axis params Dict.** Axis params for function f3"
    "``'mirror_x'``", "``False``", "**Boolean.** If x-axis is mirrored"
    "``'mirror_y'``", "``False``", "**Boolean.** If y-axis is mirrored"
    "``'proportion'``", "``1.0``", "**Float.** Factor for spacings between lines"
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Unknown values are given with strings, e.g. 'x'. An example:``[[0.8, 0.1, 'x'], ['x', 0.2, 1.0]]`` "



General parameters
^^^^^^^^^^^^^^^^^^

See :ref:`main_params` for top level main parameters.
