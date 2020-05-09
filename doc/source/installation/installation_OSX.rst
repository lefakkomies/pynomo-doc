Python 2.7.x OSX Installation
=============================
In OSX `Macports <https://www.macports.org>`_ is an effective tool to manage open-source software. In the following a
MacPorts environment is set for Python and pyNomo. `sudo` runs the commands as super-user and requires it's password to be given.

First install python 2.7

.. code-block:: bash

    $ sudo port install python27

One can list available python versions on the system with command

.. code-block:: bash

    $ sudo port select --list python

Select MacPorts python 2.7

.. code-block:: bash

    $ sudo port select --set python python27

Install python package index tool (pip)

.. code-block:: bash

    $ sudo port install py27-pip

and set it active

.. code-block:: bash

    $ sudo port select --set pip pip27

Now python environment should be correct to be run from ``/opt/local/Library/...``. Now install other required packages.

.. code-block:: bash

    $ sudo port install py27-numpy
    $ sudo port install py27-scipy
    $ sudo port install py27-pyx
    $ sudo port install py27-six
    $ sudo pip install pynomo



