Python 3.5 OSX Installation
===========================
In OSX `Macports <https://www.macports.org>`_ is an effective tool to manage open-source software. In the following a
MacPorts environment is set for Python and pyNomo. `sudo` runs the commands as super-user and requires it's password to be given.

First install python 3.5

.. code-block:: bash

    $ sudo port install python35

One can list available python versions on the system with command

.. code-block:: bash

    $ sudo port select --list python

Select MacPorts python 2.7

.. code-block:: bash

    $ sudo port select --set python3 python35

Install python package index tool (pip)

.. code-block:: bash

    $ sudo port install py35-pip

and set it active (this sets it system-wide, if you are using also python2, consider twice)

.. code-block:: bash

    $ port select --set pip pip35

Now python environment should be correct to be run from ``/opt/local/Library/...``. Now install other required packages.

.. code-block:: bash

    $ sudo port install py35-numpy
    $ sudo port install py35-scipy
    $ sudo port install py35-scipy
    $ sudo port install texlive
    $ sudo port install texlive-fonts-recommended


If you set pip active in whole system, run:

.. code-block:: bash

    $ sudo pip install pynomo
    $ sudo pip install --allow-external pyx pyx

If not, check where pip is located and run for example (check your pip path)

.. code-block:: bash

    $ sudo /opt/local/bin/pip install pynomo
    $ sudo /opt/local/bin/pip install --allow-external pyx pyx

