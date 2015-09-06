Windows installation
====================

#. Download and install `python 2.7.x <https://www.python.org>`_ from `www.python.org/downloads/ <https://www.python.org/downloads/>`_ . pyNomo is not yet compatible with python 3.x.x

#. Download and install `MIKTeX <http://miktex.org>`_ LaTeX -distribution from `http://miktex.org/download <http://miktex.org/download>`_.

#. Download and install `numpy <http://www.numpy.org>`_ from `sourceforge.net/projects/numpy <http://sourceforge.net/projects/numpy/files/latest/download?source=files>`_.

#. Download and install `scipy <http://www.scipy.org>`_ from `sourceforge.net/projects/scipy <http://sourceforge.net/projects/scipy/files/latest/download?source=files>`_.

#. Download and install `PIL (python imaging library) <http://www.pythonware.com/products/pil/>`_ from `http://effbot.org/downloads/ <http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe>`_. PIL is required by some pyx packages. pynomo might work without PIL.


pyx (python graphics package) installation is more tricky. Either


* Download `pyx 0.12.1 (python graphics package) <http://pyx.sourceforge.net>`_ from `http://sourceforge.net/projects/pyx/files/pyx/0.12.1/PyX-0.12.1.tar.gz/download <http://sourceforge.net/projects/pyx/files/pyx/0.12.1/PyX-0.12.1.tar.gz/download>`_
* Uncompress the file `PyX-0.12.1.tar.gz` using for example `7-zip <http://www.7-zip.org>`_.
* Open command prompt (cmd) and go to the uncompressed folder that contains file `setup.py`.
* run command ``python setup.py install``

or cross your fingers and just run::

    > pip install --allow-external pyx pyx

on command prompt with administrative rights.


Finally pyNomo is installed either by downloading installer from  `http://sourceforge.net/projects/pynomo/ <http://sourceforge.net/projects/pynomo/files/pynomo/>`_ and by running it. Other choice to try is to run::

    > pip install pynomo

on command line. Tedious, huh! If you find simpler Windows recipe, please email it to the maintainer of the project.
