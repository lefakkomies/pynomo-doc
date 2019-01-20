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

        :math:`d = {e\times c}`

Where :math:`e` (economy) was expressed in terms of distance travelled per unit volume of fuel.  This is precisely what we want but we need to adjust the scales for American units of measure.  This is accomplished by:

#. *Converting* the minimum (:code:`u_min`) and maximum (:code:`u_max`) values in the axis to match those in the SI unit axis.
#. *Aligning* the distance and fuel consumed axis so that they match the height of the SI unit axis.
#. *Tagging* the distance and fuel scales so that they align horizontally with their metric system counterparts. 

Thus our three new scales are defined as follows:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 39
    :lines: 39-51

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 66
    :lines: 66-78

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 92
    :lines: 92-104

Tags are also added to the SI units at lines 29 and 82.

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 27
    :lines: 27-30

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 80
    :lines: 80-83

Notice no alignment function or tag is specified for the :code:`eff_US` axis.  None are required because this axis is a function of the :code:`dist_US` and :code:`fuel_US` axis which are already scaled appropriately therefore its alignment is automatic.  

A new block is created to link the three new scales with an isopleth defined at line 119.

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 114
    :lines: 114-120

Since all blocks must define the same number of isopleths, we add one at line 111:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 106
    :lines: 106-112

Finally, the new block is added to the :code:`block_params` key at line 126:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 122
    :lines: 122-131

This nomogram holds useful features.  The individual scales for distance, fuel consumption and fuel economy can be used on their own to convert from one system of measurement to another.  Another feature is the ability to use variables from different system of units (e.g. kilometres and US gallons) and calculate fuel economy in either miles per gallon or litres per 100 km.

**************************
Generated nomogram
**************************

.. image:: images/tutorial2.*
