Big picture of nomograph construction
=====================================
Nomographs of PyNomo are
constructed by writing a python script that defines the nomograph parameters and
initializes class ``Nomographer(parameters)`` to build the nomograph.

Nomograph is constructed by defining axes that are used to
build blocks. If there are more than one block,  they are aligned with each other in order to
construct the nomograph.

A simple example of pseudocode of typical PyNomo structure is the
following:

.. code:: python

    from pynomo.nomographer import *  # this loads the needed pynomo class
    # define block 1
    axis_params_1_for_block_1 = {...}
    axis_params_2_for_block_1 = {...}
    axis_params_3_for_block_1 = {...}
    block_1 = {...}

    # define block 2
    axis_params_1_for_block_2 = {...}
    axis_params_2_for_block_2 = {...}
    axis_params_3_for_block_2 = {...}
    block_2 = {...}

    # define nomograph
    main_params = { 'filename': 'filename_of_nomograph.pdf',  # filename of output
                    'block_params': [block_1,block_2],        # the blocks make the nomograph
                    'transformations':[('scale paper',)],     # these make (projective) transformations for the canves
                    }
    # create nomograph
    Nomographer(main_params)

It is to be noted that nomograph is defined as python dictionaries that
constitute one main dictionary that is passed to Nomographer class.

Axes
^^^^

A nomograph consist in simple terms of axes (or scales) that are positioned in a way to fulfil the equation to be graphed.
Axes (or grids or graphs) are the leafs that build the tree of a nomograph.
Defining axes and their appearance is major work in nomograph
construction. Different possibilities are illustrated in Axes chapter.

Blocks
^^^^^^

Blocks relate axes to each other. Each block fulfils some equation where axes are the variables.
The following blocks below with corresponding equations are the core of PyNomo.
These are used as easy
building blocks for nomograph construction. If these do not suffice one
can build as complex nomograph as one wishes by using determinants in type 9.

.. |type1image| image:: types/images/ex_type1_nomo_1.*
    :height: 100px

.. |type2image| image:: types/images/ex_type2_nomo_1.*
    :height: 100px

.. |type3image| image:: types/images/ex_type3_nomo_1.*
    :height: 100px

.. |type4image| image:: types/images/ex_type4_nomo_1.*
    :height: 100px

.. |type5image| image:: types/images/ex_type5_nomo_1.*
    :height: 100px

.. |type6image| image:: types/images/ex_type6_nomo_1.*
    :height: 100px

.. |type7image| image:: types/images/ex_type7_nomo_1.*
    :height: 100px

.. |type8image| image:: types/images/ex_type8_nomo_1.*
    :height: 100px

.. |type9image| image:: types/images/ex_type9_nomo_1.*
    :height: 100px

.. |type10image| image:: types/images/ex_type10_nomo_1.*
    :height: 100px

.. only:: latex

    .. tabularcolumns:: |p{2cm}|p{7cm}|p{5cm}|
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


.. only:: html

    ========================== ======================================================================= ===================================
     :ref:`type1_ref`          :math:`F_1(u_1)+F_2(u_2)+F_3(u_3)=0 \,`                                 |type1image|
     :ref:`type2_ref`          :math:`F_1(u_1)=F_2(u_2) F_3(u_3) \,`                                   |type2image|
     :ref:`type3_ref`          :math:`F_1(u_1)+F_2(u_2)+\cdots+F_N(u_N)=0`                             |type3image|
     :ref:`type4_ref`          :math:`\frac{F_1(u_1)}{F_2(u_2)}=\frac{F_3(u_3)}{F_4(u_4)}`             |type4image|
     :ref:`type5_ref`          :math:`F_1(v) = F_2(x,u). \,`                                           |type5image|
     :ref:`type6_ref`          :math:`u=u \,`                                                          |type6image|
     :ref:`type7_ref`          :math:`\frac{1}{F_1(u_1)}+\frac{1}{F_2(u_2)}=\frac{1}{F_3(u_3)} \,`     |type7image|
     :ref:`type8_ref`          :math:`y = {F(u)} \,`                                                   |type8image|
     :ref:`type9_ref`          :math:`\begin{vmatrix}F_1(u_1[,v_1])& G_1(u_1[,v_1]) & H_1(u_1[,v_1])\\ |type9image|
                               F_2(u_2[,v_2])& G_2(u_2[,v_2]) & H_2(u_2[,v_2]) \\
                               F_3(u_3[,v_3])& G_3(u_3[,v_3]) & H_3(u_3[,v_3]) \end{vmatrix} = 0`
     :ref:`type10_ref`          :math:`F_1(u)+F_2(v)F_3(w)+F_4(w)=0 \,`                                 |type10image|
    ========================== ======================================================================= ===================================




Combination of blocks
^^^^^^^^^^^^^^^^^^^^^

If a nomograph consists of many equations that are aligned, a compound nomograph is constructed. Chapter compound nomograph
discusses block aligment in detail.

Transformations
^^^^^^^^^^^^^^^

Scales shall be transformed in order to use given space (paper) optimally. Chapter Transformations discusses transformations.


