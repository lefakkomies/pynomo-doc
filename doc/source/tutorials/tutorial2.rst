Tutorial 2: Vehicle economy calculator (Metric and US)
-----------------------------------

**************************
Objective
**************************

Create a nomogram similar to the one in Tutorial 1 but add scales for American units of measure (miles and US gallons).  This tutorial will cover:

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

#. *Converting* the minimum (:code:`u_min`) and maximum (:code:`u_max`) values in the axis to match those in a SI unit axis.
#. *Aligning* the distance and fuel consumed axis so that they match the height of the SI unit axis.
#. *Tagging* the distance and fuel scales so that they align horizontally with their metric system counterparts. 

Thus our three new scales are defined as follows:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 37
    :lines: 37-49

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 64
    :lines: 64-76

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 90
    :lines: 90-102

Tags are also added to the SI units at lines 27 and 80.

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 25
    :lines: 25-28

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 78
    :lines: 78-81

Notice no alignment function or tag is specified for the :code:`eff_US` axis.  None are required because this axis alignment is a function of the :code:`dist_US` and :code:`fuel_US` axis which are already scaled appropriately.  

A new block is created to link the three new scales with an isopleth defined at line 117.

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 112
    :lines: 112-118

Since every block in a nomogram must have the same number of isopleths, we add one at line 109:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 104
    :lines: 104-110

Finally, the new block is added to the :code:`block_params` key at line 124:

.. literalinclude:: source_code/tutorial2.py
    :linenos:
    :language: python
    :lineno-start: 120
    :lines: 120-129

This nomogram holds interesting features.  The individual scales for distance, fuel consumption and fuel economy can be used on their own to convert from one system of measurement to another.  Another is the inherent ability to use variables from different system of units (e.g. kilometres and US gallons) and calculate fuel economy in either miles per gallon or litres per 100 km.

**************************
Generated nomogram
**************************

.. image:: images/tutorial2.*

