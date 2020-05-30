Axes by example
---------------

Axes are fundamental building blocks of nomographs. The following code uses minimal axis definion ``N_params`` that is
rendered as a linear scale illustrated below. The range of values axis represents is defined with keywords ``u_min``
and ``u_max``. ``title`` sets title string for the axis. Key part of the nomograph is the functional form of the axis.
In the example below it is defined with keyword ``function`` and is given as a function. Different types of blocks assume different keywords
of axis functions. For example types 1, 2 and 3 take keyword ``function`` but type 9 takes either ``f``, ``g``, ``h`` or
``f_grid``, ``g_grid``, ``h_grid`` keywords. So one have to define axis parameters compatible with the used block type.
In the examples below Type 8 is used as block to taking axis definition because it is the simplest one.


Linear scale (``'scale_type':'linear'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. _axes_ex_code_ref:

Here we start with the simplest axis. It has by default scale ``'scale_type':'linear'`` that is simple linear scale.

.. literalinclude:: ./codes/ex_axes_1.py
    :encoding: latin-1
    :linenos:
    :name: ex_axes_1-py


.. image:: images/ex_axes_1.*
    :height: 600px



Because the example above looked little too busy or packed, we reduce the ticks by using only three different tick levels
``'tick_levels':3`` and two tick text levels ``'tick_text_levels':2``. Tick side relative to the final drawing is set to
left using ``'tick_side':'left'``.

.. literalinclude:: ./codes/ex_axes_2.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_2.*
    :height: 600px

Title position can be shifted in both x- and y-directions. In the following we shift it using key-values
``'title_x_shift':-1.0`` and ``'title_y_shift':0.5``. Units are here centimeters.

.. literalinclude:: ./codes/ex_axes_3.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_3.*
    :height: 600px


Sometimes single level of axis definitions is not enough. We might want to add more ticks in some additional range of the axis.
Keyword ``'extra_params'`` helps here. Value for this key is an array of dictionaries that modify given params in the
given range set by ``u_min`` and ``u_max``. In the following example we define additional ranges with more ticks in ranges
5.0..10.0 and 9.0..10.0. We also draw title this time to center using ``'title_draw_center:True``.

.. literalinclude:: ./codes/ex_axes_4.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_4.*
    :height: 600px

Color can be used to tune visual appearance of the axis. In the following example we tune colors with self-explaining
keywords ``'axis_color'``, ``'text_color'`` and ``'title_color'``. Additional titles are set by using keyword ``'extra_titles'``
with value of an array of dictionaries that can take keywords ``'dx'`` and ``'dy'`` as relative position to main title.
Value of keyword ``'text'``sets the title text and ``'pyx_extra_defs'`` can be used to give additional parameters for pyx rendering
that is only option in current release. In the example numbers are formatted to have one three digits before comma and
and one digit after comma using ``'text_format':r"$%3.1f$ "``.


.. literalinclude:: ./codes/ex_axes_4_1.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_4_1.*
    :height: 600px

Manual point scale (``'scale_type':'manual point'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sometimes axes have to be defined manually. One option is to use manual point scale type with ``'scale_type':'manual point'``
and define the points as a dict to keyword ``'manual_axis_data'``.


.. literalinclude:: ./codes/ex_axes_5.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_5.*
    :height: 600px

Manual line scale (``'scale_type':'manual line'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similarly other option is to use manual line scale type with ``'scale_type':'manual line'`` that draws main scale line
and ticks. Drawn ticks are defined as a dict to keyword ``'manual_axis_data'`` as above example.

.. literalinclude:: ./codes/ex_axes_6.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_6.*
    :height: 600px

Combining manual lines and  a linear scale.

.. literalinclude:: ./codes/ex_axes_7.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_7.*
    :height: 600px

Manual arrows  (``'scale_type':'manual arrow'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Manual arrows can be used to point values in the scale using arrows.

.. literalinclude:: ./codes/ex_axes_7_1.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_7_1.*
    :height: 600px

Manual function  (``'function_x'`` and ``'function_y'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If one wants to explicitly draw scale in xy-scale, parameters ``'function_x'`` and ``'function_y'`` can be used
in conjunction with block type 8. In the following example circular scale is drawn.

.. literalinclude:: ./codes/ex_axes_8.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_8.*
    :height: 600px

In the following we fine-tune the appearance of the scale. Tick lengths are explicitly given with params ``'grid_length_x'``
(note name with bad logic), text sizes are tuned with params ``'text_size_x'`` and distance of text to the scale is set using
``'text_distance_x'``. ``'full_angle'`` parameter allows text to be drawn also upside down and text angle is rotated with
``'extra_angle'``.

.. literalinclude:: ./codes/ex_axes_8_1.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_8_1.*
    :height: 600px

Linear scale (``'scale_type':'log'``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Often one needs to use logarithmic functions in scales and ``'scale_type':'log'`` makes some optimizations for this kind
of scale appearance.

.. literalinclude:: ./codes/ex_axes_9.py
    :encoding: latin-1
    :linenos:

.. image:: images/ex_axes_9.*
    :height: 600px

Smart scales (``'scale_type':'smart linear'``, ``'scale_type':'smart log'``)
^^^^^^^^^^^^
Linear and log scales just plot ticks and texts as given with params ``'tick_levels'`` and ``'tick_text_levels'``. Often
this approach generates busy scales with overlapping texts and too dense ticks. Better approach is to use smart
linear scales ``'scale_type':'smart linear'`` or smart log scales ``'scale_type':'smart log'`` These scales check that
tick and text distances does not go below given thresholds (``'tick_distance_smart'`` and  ``'text_distance_smart'``.
TODO: example to use smart scales.
