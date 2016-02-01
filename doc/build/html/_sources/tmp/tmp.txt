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