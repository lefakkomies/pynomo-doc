Python 3 Linux installation
===========================

In `Debian <https://www.debian.org>`_
Linux distribution and in its `derivatives <https://en.wikipedia.org/wiki/List_of_Linux_distributions>`_ (for example `Ubuntu <http://ubuntu.com/>`_  and `Raspbian <https://www.raspbian.org>`_) pynomo can be installed using `apt-get` with the following commands.
`sudo` runs the commands as super-user and requires it's password to be given.

.. code-block:: bash

    $ sudo apt-get -y install python3
    $ sudo apt-get -y install python3-pip
    $ sudo apt-get -y install python3-numpy
    $ sudo apt-get -y install python3-scipy
    $ sudo apt-get -y install texlive-latex-base
    $ sudo apt-get -y install texlive-fonts-recommended
    $ sudo pip install pynomo
    $ pip3 install --allow-external pyx pyx
    $ pip3 install pynomo

