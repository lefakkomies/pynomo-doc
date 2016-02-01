Example Photography exposure
============================

Theory and background
---------------------

This example illustrates how exposure in photography depends on factors:
latitude, time of day, day of year, weather, composition. It relates
these to camera settings: film speed (e.g. ISO 100), aperture and
shutter speed. The mathematical approach and model is taken from book
written by V. Setälä. [1]_ This book illustrates the approach as
nomographs but they are different compared with the one generatated
here. Book uses shadow length, but we break shadow length into time,
date and latitude via solar zenith angle.

The basic equation in Setälä (pp.492-494) can be extracted and
written as

.. math:: FS-L-A-W+C+T=0 \,
    :label: setala1

where parameters of :eq:`setala1` are listed below:


.. list-table::
    :widths: 10 20 50
    :stub-columns: 0

    * - :math:`FS\,`
      - Film speed
      - DIN value that equals :math:`10 \log (S) +1 \,`,where S is ISO FILM speed
    * - :math:`T\,`
      - shutter time
      - :math:`10 \log \left( \frac{t}{1/10}\right)`
    * - :math:`A\,`
      - aperture
      - :math:`10 \log \left(\frac{N^2}{3.2^2}\right)`
    * - :math:`L\,`
      - shadow length (in steps)
      - two times (shadow length)/(person length) :math:`= 2 \arctan ( \phi) \,`, where :math:`\phi \,` is solar zenith angle.
    * - :math:`W\,`
      - weather
      - Clear sky, Cumulus clouds: 0, Clear sky: 1, Sun through clouds: 3, Sky light gray: 6, Sky dark gray: 9, Thunder-clouds cover sky: 12
    * - :math:`C\,`
      - Composition
      - Person under trees: -6, Inside forest : -4, Person in shadow of wall : -1, Person at open place; alley under trees : 2, Buildings; street : 5, Landscape and front matter : 7, Open landscape : 9, Snow landscape and front matter; beach : 11,Snow field; open sea : 13, Clouds : 15



It is to be noted that Setälä has stops ten times base-10 logarithmic.
Today we think stops in base-2 logarithmic.

Shadow lenght
^^^^^^^^^^^^^

Calculation of shadow length as a function of day of year, time of day
and latitude is according to  [2]_. Following equations are used. For
fractional year (without time information) we take

:math:`\gamma = (day-1+0.5)2\pi /365.`

For time offset (eqtime) we use equation (in minutes)

:math:`TO = 229.18(0.000075+0.001868\cos(\gamma)-0.032077\sin(\gamma)-0.014615\cos(2\gamma)-0.040849\sin(2\gamma))`

to calculate that error is below 17 minutes for time axis. We assume
that sun is at heightest point at noon and this is the error and
approximation. We calculate stops in logarithmic scale and in this case
we do not need very accurate equations for time. For declination we use
equation

.. math::
    :nowrap:
    \begin{eqnarray*}
     D=0.006918-0.399912\cos(\gamma)+0.070257\sin(\gamma)-0.006758\cos(2\gamma) \\
     +0.000907\sin(2\gamma)-0.002697\cos(3\gamma)+0.00148\sin(3\gamma)
     \end{eqnarray*}

and for hour angle

:math:`ha=(60h+\overline{TO})/4-180. \,`

Solar zenith angle (:math:`\phi \,`), latitude (LAT),
declination (D) and hour angle (ha) are connected with equation:

:math:`\cos (\phi ) = \sin(LAT)sin(D)+\cos(LAT)\cos(D)\cos(ha). \,`

This is in our desired form as a function of hour (h), day (day),
latitude (LAT), solar zenith angle (:math:`\phi \,`):

:math:`\cos (\phi ) = \sin(LAT)sin(D(\gamma(day)))+\cos(LAT)\cos(D(\gamma(day)))\cos(ha(h)) \,`.

In practice illuminance of flat surface on earth depends on solar zenith
angle as :math:`\cos(\phi)\,`. Setälä uses shadow length that is
easily measurable, but scales incorrectly, as value is proportional to
:math:`\tan(\phi)\,`. Also Setälä sums linear value with
logarithmic ones as a practical approximation. To correct these
assumptions, here we assume that values for shadow length 1 and 10 for Setälä
are reasonable, and an equation that scales logarithmically is found:

:math:`L = 0.33766 - 13.656 \log10 (\cos(\phi)) \,`

that gives :math:`L=1\,` for :math:`\phi = 26.565 =\arctan(1/2)\,` and :math:`L=10\,` for :math:`\phi = 78.69 =\arctan(10/2).\,`

.. [1]
   Vilho Setälä: "Valokuvaus", Otava 1940.

.. [2]
   http://www.srrb.noaa.govhighlights/sunrise/solareqns.PDF

Construction of the nomograph
-----------------------------

The presented equation is the following:

.. math::
    :nowrap:

    \begin{eqnarray*}
        FS - \{0.33766 - 13.656 \log_{10}[ \sin (LAT)\sin (D(\gamma(day)))+\cos (LAT)\cos (D(\gamma(day)))\cos (ha(h))]\}\\
        - A - W + C + T = 0.
    \end{eqnarray*}


In order to construct the nomograph, we split the equation into four blocks and an additional block to present values as EV100.

.. tabularcolumns:: |p{14cm}|p{2cm}|
.. csv-table:: Main equation split into blocks for the nomograph.
    :class: longtable
    :header: "Explanation", "Type"
    :widths: 40, 40

    "
    .. math::
        x_1 \equiv \cos(\phi)=\sin(LAT)sin(D(\gamma(day)))+\cos(LAT)\cos(D(\gamma(day)))\cos(ha(h))\,

    formed into determinant:

    .. math::
        {
        \begin{vmatrix}
                0  & \cos(\phi) & 1 \\
               \frac{\cos(LAT)\cos(D(\gamma(day)))}{1+(\cos(LAT)\cos(D(\gamma(day))))}  & \frac{\sin(LAT)\sin(D(\gamma(day)))}{1+(\cos(LAT)\cos(D(\gamma(day))))} & 1 \\
               1  & -\cos(ha(h)) & 1 \\
        \end{vmatrix} = 0 }

    ", "Type 9"
    "
    .. math::
        C_1 \equiv L+W = 0.006918-13.656 \log_{10}(x_1)+W

    split into two equations for contour construction:

    .. math::
        y_1 = C_1 \,

    .. math::
        y_1 = 0.006918-13.656  \log_{10}(x_1)+W
     ", "Type 5"
    "
    .. math::
        C_2 \equiv L+W+C = C_1+C

    split into two equations for contour construction:

    .. math::
        y_2 = C_2

    .. math::
        y_2 = C_1+C

    ", "Type 5"
    "
    .. math::
        C_2 = FS-A+T

    equals

    .. math::
        C_2 -(10 \log_{10}(S)+1.0)+10 \log_{10}\left(\frac{N^2}{3.2^2} \right)-10 \log_{10}\left( \frac{1/t_i}{1/10}\right)=0,

    where

    .. math::
        t_i\equiv 1/t

    is inverse shutter time.", "Type 3"
    "
    Additional EV100 scale by using relation

    .. math::
        C_2 =(-EV_{100}+13.654)/0.3322

    ","Type 8"
    "
    Maximum focal length calculator according to equation

    .. math::
        t_i / f = FL

    written as

    .. math::
        -10 \log_{10}\left( \frac{1/t_i}{1/10}\right) - 10 \log_{10}\left( \frac{f}{10} \right)  -10 \log_{10}\left( FL \right) = 0

    in order to align correctly with previous equation.  The values for the factor f  are: DSLR (3/2), 35mm (1),
    DSLR image stabilization (3/8) and 35mm image stabilization (1/8).", "Type 1"



Generated nomograph
-------------------

.. image:: ex_photo_exposure.*


Source code
-----------

.. literalinclude:: ex_photo_exposure.py
    :encoding: latin-1
    :linenos:
    :lines: 1-4, 20-



