.. _type9_ref:

Type 9
======


Type 9 is "general determinant" nomograph that has functional
relationship:

.. math::
    \begin{vmatrix}
    F_1(u_1[,v_1])      & G_1(u_1[,v_1]) & H_1(u_1[,v_1])      \\
    F_2(u_2[,v_2])      & G_2(u_2[,v_2]) & H_2(u_2[,v_2]) \\
    F_3(u_3[,v_3])      & G_3(u_3[,v_3]) & H_3(u_3[,v_3])
    \end{vmatrix} = 0.

This is the basic building block for line nomographs. Notation
:math:`u[,v]\,` is to be understood such that if v is defined´, a grid
is constructed for the row, otherwise a normal scale with variable u.

Simple example
--------------

This simple example plots nomograph for equation in determinant form:

.. math::
    \begin{vmatrix}
    0      & u_1 & 1      \\
    u_2+2      & 2v_2+5 & 1 \\
    4      & u_3 & 1 \end{vmatrix} = 0

Generated nomograph
^^^^^^^^^^^^^^^^^^^

.. image:: images/ex_type9_nomo_1.*

Source code of simple example of type 9
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ex_codes/ex_type9_nomo_1.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-




Parameters for type 9
---------------------

Axis parameters
^^^^^^^^^^^^^^^

.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific axis parameters for type 9 grid axis
    :header: "parameter key", "default value", "**type**, explanation"
    :widths: 10, 10, 60

           "``'grid'``", "--", "**Bool.** :code:`True` because this is grid."
       "``'f'``", "--", "**func(u,v).** F function in determinant. For example ``lambda u,v:u+v``"
       "``'g'``", "--", "**func(u,v).** G function in determinant. For example ``lambda u,v:u+v``"
       "``'h'``", "--", "**func(u,v).** H function in determinant. For example ``lambda u,v:u+v``"
       "``'u_start'``", "--", "u start when drawing v=const line"
       "``'u_stop'``", "--", "u stop when drawing v=const line"
       "``'v_start'``", "--", "v start when drawing u=const line"
       "``'v_stop'``", "--", "v stop when drawing u=const line"
       "``'u_values'``", "--", "List of grid lines u=const. For example ``[0.0,0.25,0.5,0.75,1.0]``"
       "``'v_values'``", "--", "List of grid lines v=const. For example ``[0.0,0.25,0.5,0.75,1.0]`"
       "``'text_prefix_u'``", "--", "Text prefix for u before value"
       "``'text_prefix_v'``", "--", "Text prefix for v before value"
       "``'v_texts_u_start'``", "``False``", "If v-texts are in u start side"
       "``'v_texts_u_stop'``", "``True``", "If v-texts are in u stop side"
        "``'u_texts_v_start'``", "``False``", "If u-texts are in v start side"
        "``'u_texts_v_stop'``", "``True``", "If u-texts are in v stop side"
        "``'u_line_color'``", "``color.rgb.black``", "**Color.** u line color"
        "``'v_line_color'``", "``color.rgb.black``", "**Color.** v line color"
        "``'u_text_color'``", "``color.rgb.black``", "**Color.** u text color"
        "``'v_text_color'``", "``color.rgb.black``", "**Color.** v text color"
        "``'text_distance'``", "0.25", "**Float.** Text distance"
        "``'circles'``", "``False``", "**Boolean.** If marker circles to crossings"
        "``'extra_params'``", "--", "**List of Dicts.** List of params to be drawn."

See :ref:`common_axis_params` for other parameters.


Block parameters
^^^^^^^^^^^^^^^^


.. tabularcolumns:: |p{4cm}|p{4cm}|p{7cm}|
.. csv-table:: Specific block parameters for type 9
    :header: "parameter", "default value", "explanation"
    :widths: 10, 10, 60

    "``'block_type'``", "``'type_9'``", "**String.** This is type 9 block"
    "``'width'``", "10.0", "**Float.** Block width (to be scaled)"
    "``'height'``", "10.0", "**Float.** Block height (to be scaled)"
    "``'f1_params'``", "--", "**Axis params Dict.** Axis params for function f1"
    "``'f2_params'``", "--", "**Axis params Dict.** Axis params for function f2"
    "``'f3_params'``", "--", "**Axis params Dict.** Axis params for function f3"
    "``'mirror_x'``", "``False``", "**Boolean.** If x-axis is mirrored"
    "``'mirror_y'``", "``False``", "**Boolean.** If y-axis is mirrored"
    "``'transform_ini'``", "``False``", "**Boolean.** If row 1 and row 3 end and start are to be transformed to be in rectangle corners. If True, be sure that 'u_min_trafo' and 'u_max_trafo' are defined."
    "``'isopleth_values'``", "``[[]]``", "** List of list of isopleth values.** Grid values are given with tuple (a,b) and are not solved. Unknown values are given with strings, e.g. 'x'. An example:``[[0.8,(0.1,0.2),'x'], ['x',(0.1,0.2),1.0]]`` "



General parameters
^^^^^^^^^^^^^^^^^^

See :ref:`main_params` for top level main parameters.


