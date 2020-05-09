Python 3.5 Windows installation
=================================

#. Download and install `python 3.5.x <https://www.python.org>`_ from `www.python.org/downloads/ <https://www.python.org/downloads/>`_ .

#. Download and install `MIKTeX <http://miktex.org>`_ LaTeX -distribution from `http://miktex.org/download <http://miktex.org/download>`_.

#. Download and install `numpy <http://www.numpy.org>`_ from ``.net/projects/numpy <http://sourceforge.net/projects/numpy/files/latest/download?source=files>`_.

#. Download and install `scipy <http://www.scipy.org>`_ from `sourceforge.net/projects/scipy <http://sourceforge.net/projects/scipy/files/latest/download?source=files>`_.


pyx (python graphics package) installation is more tricky. Either


* Download `pyx 0.15 (python graphics package) <https://pyx-project.org>`_ from `https://pypi.python.org/packages/source/P/PyX/PyX-0.15.tar.gz <https://pypi.python.org/packages/source/P/PyX/PyX-0.15.tar.gz>`_
* Uncompress the file `PyX-0.15.tar.gz` using for example `7-zip <http://www.7-zip.org>`_.
* Open command prompt (cmd) and go to the uncompressed folder that contains file `setup.py`.
* run command ``python setup.py install``

or cross your fingers and just run::

    > pip install --allow-external pyx pyx

on command prompt with administrative rights.


Finally pyNomo is installed either by downloading installer from  `http://sourceforge.net/projects/pynomo/ <http://sourceforge.net/projects/pynomo/files/pynomo/>`_ and by running it. Other choice to try is to run::

    > pip install pynomo

on command line. Tedious, huh! If you find simpler Windows recipe, please email it to the maintainer of the project.
