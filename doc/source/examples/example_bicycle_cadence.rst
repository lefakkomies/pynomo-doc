Bicycle Cadence
============================

Theory and background
---------------------

Determining a bicycle’s speed in relation to the rider’s cadence (or vice versa) is important for riding enjoyment.  Choosing the correct gear ratio can help the rider maximize their speed with a comfortable cadence. A bicycle’s speed is the product of the wheel diameter (typically 700mm), the wheel’s rotation rate (in rpm) and :math:`\pi`. The wheel’s rotation rate is a function of the rider’s cadence and the front to rear gear ratio.

As in the previous example, pairs of discrete values such as the number of teeth on the front and rear sprokets are easily represented on a Type 5 block.  This nomograph combines a Type 5 block (to calculate gearing ratio) with a pair of Type 2 blocks to calculate the bicycle’s speed given a front derailer and rear cage settings. 

Generated nomograph
-------------------

.. image:: ex_bicycle_cadence.*


Source code
-----------

.. literalinclude:: ex_bicycle_cadence.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-


