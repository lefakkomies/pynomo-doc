Software documentation
======================
Nomographs of PyNomo are
constructed by writing a python script that defines the nomograph and
calls class Nomographer to build the nomograph.

Nomograph is constructed by defining axis parameters that are used to
build a block. Many blocks are possibly aligned with each other and
construct the nomograph.

A simple example of pseudocode of typical PyNomo structure is the
following:

.. code:: python

    from pynomo.nomographer import * # this loads the needed pynomo class
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
    main_params={
                  'filename':'filename_of_nomograph.pdf',  # filename of output
                  'block_params':[block_1,block_2],        # the blocks make the nomograph
                  'transformations':[('scale paper',)],    # these make (projective) transformations for the canves
                  }
    # create nomograph
    Nomographer(main_params)

It is to be noted that nomograph is defined as python dicts that
constitute one dict that is passed to Nomographer class.

Basic blocks
------------

The following blocks are the core of PyNomo. These are used as easy
building blocks for nomograph construction. If these do not suffice one
can build as complex nomograph as one wishes by using determinants in
`type 9 <type 9>`__.

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





Axes
----

Defining axes and their appearance is major work in nomograph
construction. Different possibilities are illustrated in `examples of
axes parameters <examples of axes parameters>`__.

Combination of blocks
---------------------

If a nomograph consists of many equations that are aligned, a `compound
nomograph <compound nomograph>`__ is constructed.

Transformations
---------------

Scales shall be `transformed <transformations>`__ in order to tune the
appearance.

Manual
------

Article ''`"Creating Nomograms with the PyNomo Software"'' by Ron
Doerfler <http://www.myreckonings.com/wordpress/>`__ is a detailed
manual for using PyNomo.
