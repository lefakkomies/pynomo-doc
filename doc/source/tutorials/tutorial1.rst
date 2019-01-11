Tutorial 1: Vehicle economy calculator
-----------------------

*********
Objective
*********

Construct an "N" type nomogram to calculate a vehicle's range, fuel consumption or fuel economy given any two of these values.  The nomogram will be built using linear scales.

**************************
Nomogram construction
**************************

Nomogram construction involves several steps.  The first is always to identify the variables and their relationship. In this tutorial we need to consider three variables:

* distance (:math:`d`) measured in kilometres,
* fuel consumed (:math:`c`) measured in litres, and
* fuel economy  (:math:`e`) measured in kilometres driven per litre consumed.

The relationship between these variables is:

    :math:`d = {e\times c}`

This equation satisfies the form for a Type 2 nomogram (see section 6.2) as follows:

    :math:`F_1(u_1) = {F_2(u_2)F_3(u_3)}`

Where:

    :math:`u_1 = d`

    :math:`u_2 = e`

    :math:`u_3 = c`


All scales are linear and we choose a reasonable range of values (:code:`u_min` and :code:`u_max`) for each axis.  

.. literalinclude:: source_code/tutorial1a.py
    :linenos:
    :language: python
    :lineno-start: 25
    :lines: 25-54

These scales are linked into a single block as follows:

.. literalinclude:: source_code/tutorial1a.py
    :linenos:
    :language: python
    :lineno-start: 56
    :lines: 56-61


.. note:: Parameters :code:`f1_params`, :code:`f2_params` and :code:`f3_params` represent functions for :math:`u_1`, :math:`u_2` and :math:`u_3` respectively.

Finally, we  define the nomogram’s main parameters and generate the chart:

.. literalinclude:: source_code/tutorial1a.py
    :linenos:
    :language: python
    :lines: 63-71
    :lineno-start: 63


**************************
Generated nomogram
**************************

.. image:: images/tutorial1a.*

**************************
A variation on vehicle economy calculator
**************************

The previously generated nomograph is complete but doesn’t express the vehicle’s economy the way we would like.  A vehicle’s fuel economy is more often expressed in litres consumed per 100 kilometres driven, the reciprocal of the original function.  How do we do this?

Recall that

    :math:`d = {e\times c}`

Therefore ...

    :math:`{\frac{d}{c}} = e`

We express the reciprocal of the economy by rearranging the formula as follows:

    :math:`\frac{c}{d} = \frac{1}{e}`

Since our goal is to describes fuel economy in terms of litres per *100 km* multiply :math:`\frac{1}{e}` by 100.0 to achieve the correct result:

    :math:`\frac{c}{d} = \frac{100.0}{e}`

And :math:`u_2 = e` so our function for :math:`u_2` becomes

    :math:`\frac{100.0}{u_2}`

We amend line 39 accordingly and the axis definition becomes:

.. literalinclude:: source_code/tutorial1b.py
    :linenos:
    :language: python
    :lineno-start: 35
    :lines: 35-44

**************************
Generated nomogram
**************************

.. image:: images/tutorial1b.*

