Blocks
++++++

Every block in pynomo represents some equation. The blocks and their functions are listed in the following table.

.. cssclass:: table-striped
========================== ======================================================================= =========================
 :ref:`type1_ref`          :math:`F_1(u_1)+F_2(u_2)+F_3(u_3)=0 \,`                                 Three parallel lines
 :ref:`type2_ref`          :math:`F_1(u_1)=F_2(u_2) F_3(u_3) \,`                                   "N" or "Z"
 :ref:`type3_ref`          :math:`F_1(u_1)+F_2(u_2)+\cdots+F_N(u_N)=0`                              N parallel lines
 :ref:`type4_ref`          :math:`\frac{F_1(u_1)}{F_2(u_2)}=\frac{F_3(u_3)}{F_4(u_4)}`             "Proportion"
 :ref:`type5_ref`          :math:`F_1(v) = F_2(x,u). \,`                                           "Contour"
 :ref:`type6_ref`          :math:`u=u \,`                                                          "Ladder"
 :ref:`type7_ref`          :math:`\frac{1}{F_1(u_1)}+\frac{1}{F_2(u_2)}=\frac{1}{F_3(u_3)} \,`     "Angle"
 :ref:`type8_ref`          :math:`y = {F(u)} \,`                                                   "Single"
 :ref:`type9_ref`          :math:`\begin{vmatrix}F_1(u_1[,v_1])& G_1(u_1[,v_1]) & H_1(u_1[,v_1])\\ "General"
                           F_2(u_2[,v_2])& G_2(u_2[,v_2]) & H_2(u_2[,v_2]) \\
                           F_3(u_3[,v_3])& G_3(u_3[,v_3]) & H_3(u_3[,v_3]) \end{vmatrix} = 0`
 :ref:`type10_ref`          :math:`F_1(u)+F_2(v)F_3(w)+F_4(w)=0 \,`                                 One curved line
========================== ======================================================================= =========================


.. include:: type1.rst
.. include:: type2.rst
.. include:: type3.rst
.. include:: type4.rst
.. include:: type5.rst
.. include:: type6.rst
.. include:: type7.rst
.. include:: type8.rst
.. include:: type9.rst
.. include:: type10.rst