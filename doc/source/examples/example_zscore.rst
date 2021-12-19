Z Score
============================

Theory and background
---------------------

This example extends Pynomo’s versatility by using external libraries.
Python’s :code:`scipy` library is the engine behind this nomograph
which calculates the area under a normal distribution curve between
two Z scores (one negative, the other positive).

To calculatte the area between two Z scores (:math:`Z_{upper}`,
:math:`Z_{lower}`) of a normal distribution one must compute the
difference between the respective probability density functions
:math:`PDF(Z_{upper})` and :math:`PDF(Z_{lower})`. [1]_

.. image:: ex_zscore_curve.png
   :width: 500


Recall that the functional relatinship for a **Type 1** block is:

:math:`F1(u_1)+F2(u_2)+F3(u_3)=0`

and

:math:`Area = PDF(Z_{upper}) - PDF(Z_{lower})`

therefore

:math:`PDF(Z_{upper})  - Area  - PDF(Z_{lower})=0`.

Two **Type 8** axes are aligned with :math:`PDF(Z_{upper})` and
:math:`PDF(Z_{lower})` to align a Z score with its associated PDF.

Generated nomograph
-------------------

.. image:: ex_zscore.*


Source code
-----------

.. literalinclude:: ex_zscore.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-

.. [1]
	https://commons.wikimedia.org/wiki/File:The_Normal_Distribution.svg
