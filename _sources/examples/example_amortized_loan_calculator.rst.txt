
Example: Amortized loan calculator
==================================

Theory and background
---------------------

This approach of constructing an amortized loan calculator is similar to
one in Ref.  :cite:`dOcagne_1899`

Equation for amortized loan  :cite:`wiki:Amortization_calculator` is:

:math:`\frac{a}{A} = \frac{\frac{p}{100\times 12}}{1-\frac{1}{(1+\frac{p}{100\times 12})^{12n}}},`

where :math:`A` is the amount of loan, :math:`a` is monthly payment
amount, :math:`p` interest rate per year (monthly interest rate is taken
as :math:`p/12`) :cite:`wiki:annual_percentage_rate` and :math:`n` is number of years for payment.

This equation of four variables is probably impossible to present with
line and grid nomographs. For this reason a "Type 5" contour nomogram is
constructed of the right hand side of the equation and left hand
equation is just N-nomogram (Type 2). The two equations for nomogram
construction are:

:math:`x = \frac{a}{A}`

and

:math:`x = \frac{\frac{p}{100\times 12}}{1-\frac{1}{(1+\frac{p}{100\times 12})^{12n}}}.`

In practice :math:`x` is the x-coordinate of the canvas where nomogram
is constructed.

Right hand side of equation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

By defining coordinates :math:`x\,` and :math:`y\,`:

:math:`x = \frac{\frac{p}{100\times 12}}{1-\frac{1}{(1+\frac{p}{100\times 12})^{12n}}},`

:math:`y = 12n, \,` we may solve :math:`y\,` in terms of :math:`x\,` and
:math:`n\,`:

:math:`y = \frac{\log (\frac{x}{x-\frac{p}{100\times 12}})}{\log (1+\frac{p}{100 \times 12})} \,`

The previous two equations are of correct form

:math:`y = f_1(v) \,`

and

:math:`y = f_2(x,u) \,`

for type 5 nomogram. For compressing time axis (:math:`y`-axis), we
transform :math:`y \rightarrow \log y` and find

:math:`y = \log \left( \frac{\log (\frac{x}{x-\frac{p}{100\times 12}})}{\log (1+\frac{p}{100 \times 12})} \right)\,`

:math:`y = \log( 12n ). \,`

Left hand side of equation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Left hand side of equation

:math:`x = \frac{a}{A}`

is just N-nomogram

:math:`F_1(u_1) = F_2(u_2)F_3(u_3) \,`

References
^^^^^^^^^^

.. raw:: html

   <references />

Generated nomograph
-------------------

.. image:: amortized_loan.*

Source code
-----------

.. literalinclude:: ex_amortized_loan.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-


