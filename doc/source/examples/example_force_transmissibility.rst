Frequency response
============================

*Contribution: Add Lamorille*

Theory and background
---------------------
For a single degree of freedom system (driven harmonic oscillator), the force frequency response (transmissibility)
:math:`T` is defined as the ratio
between the magnitude of the transmitted force and the magnitude of the applied force.
The frequency factor (dimensionless frequency) :math:`r` is the ratio between the driving frequency and the natural frequency of the system.
The damping ratio :math:`\zeta` is a measure describing how rapidly the oscillations decay from one bounce to the next, it is specific to the system.
Vibration isolation is possible only when the frequency factor is greater than :math:`\sqrt{2}`.
Relation is according equation:

:math:`T = \sqrt{\frac{1 + (2\zeta r)^2}{(1-r^2)     + (2\zeta r)^2}}.`


Generated nomograph
-------------------

.. image:: ex_transmissibility.*


Source code
-----------

.. literalinclude:: ex_transmissibility.py
    :encoding: latin-1
    :linenos:
    :lines: 1-

