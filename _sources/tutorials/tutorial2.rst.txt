Tutorial 2: Vehicle economy calculator (Metric and US)
-----------------------------------

**************************
Objective
**************************

Create a new nomogram similar to the one shown in Tutorial 1 but add scales for American units of measure (miles and US gallons).  This tutorial will cover:

* Aligning and adjusting compatible scales.
* Modifying axis parameters (titles and tick location) to improve readability.
* Creating isopleths.
* Combining blocks into a single nomogram.

**************************
Nomogram construction
**************************

Recapping from the first part of Tutorial 1, we know that

:math:`d = {e\times c}`,

where :math:`e` (economy) was expressed in terms of distance travelled per unit volume of fuel.  This is precisely what we want but we need to adjust the scales for American units of measure.  This is accomplished by:

#. *Converting* the minimum (:code:`u_min`) and maximum (:code:`u_max`) values in the axis to match those in the SI unit axis.
#. *Aligning* the distance and fuel consumed axis so that they match the height of the SI unit axis.
#. *Tagging* the distance and fuel scales so that they align horizontally with their metric system counterparts. 

Thus our three new scales are defined as follows:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 25
    :lines: 25-37

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 52
    :lines: 52-64

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 78
    :lines: 78-90

Tags are also added to the SI units axis:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 13
    :lines: 13-16

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 66
    :lines: 66-69

Notice no alignment function or tag is specified for the :code:`eff_US` axis.  None are required because this axis is a function of the :code:`dist_US` and :code:`fuel_US` axis which are already scaled appropriately therefore its alignment is automatic.  

A new block is created to link the three new scales with an isopleth (solution line):

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 100
    :lines: 100-106

Since all blocks must contain the same number of isopleths, we add one to the :code:`block_SI` axis:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 92
    :lines: 92-98

Finally, :code:`block_US` is added to the :code:`block_params` key:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 108
    :lines: 108-115

This nomogram holds useful features.  The individual scales for distance, fuel consumption and fuel economy can be used on their own to convert from one system of measurement to another.  Another feature is the ability to use variables from different system of units (e.g. kilometres and US gallons) and calculate fuel economy in either miles per gallon or litres per 100 km.

**************************
Generated nomogram
**************************

.. image:: images/tutorial2.*

