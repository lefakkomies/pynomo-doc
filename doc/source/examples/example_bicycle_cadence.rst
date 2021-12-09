Bicycle Cadence
============================

Theory and background
---------------------

Choosing the correct gears on a bicycle allows a cyclist to maintain a comfortable cadence.  A higher
cadence helps reduce muscle fatigue [1]_ though it does put more stress on heart and
lungs.  However a lower cadence for the same power output puts more stress on the rider's knees,
hips and back. [2]_ Furthermore, cycling cadence will vary widely with beginning cyclists peddling more
slowly (60-85 rpm) and professionals exceeding 100 rpm under certain conditions.
Generally, a good cadence in cycling is between 80-100 rpm. [3]_ The
correct gear ratio can help the rider maximize their speed with a comfortable cadence.

A bicycle’s speed is the product of the wheel diameter (e.g. 700mm), 
the wheel’s rotation rate (in rpm) and :math:`\pi`. The wheel’s rotation rate is a function of
the rider’s cadence and the front to rear gear ratio. As in the previous example, pairs
of discrete values such as the number of teeth on the front and rear sprockets are
easily represented on a **Type 5** block.  This nomograph combines a **Type 5** block (to 
calculate gearing ratio) with a pair of **Type 2** blocks to calculate the rider's 
speed given their cadence and gear settings. 

Generated nomograph
-------------------

.. image:: ex_bicycle_cadence.*


Source code
-----------

.. literalinclude:: ex_bicycle_cadence.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-

..	[1]
	https://www.trainingpeaks.com/blog/what-to-consider-when-finding-your-ideal-cycling-cadence/

..	[2]
	https://thebodymechanic.com.au/cycling-cadence-what-is-it-and-why-you-should-keep-a-close-eye-on-yours/

..	[3]
	https://www.trainerroad.com/blog/whats-the-most-efficient-cycling-cadence-and-how-cadence-drills-can-make-you-faster/