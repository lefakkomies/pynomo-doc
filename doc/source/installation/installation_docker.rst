Python 2.7.x Docker installation
================================

.. note::
    Note, python 2 is not anymore supported and these instructions are more for historical reference.

`Docker <https://www.docker.com/>`_ is a platform to create a sandboxed virtualized environments. In the following example `Dockerfile` a virtualized
`Ubuntu <http://ubuntu.com/>`_ is created that has pyNomo installed with all requirements::

    # python 2.7 Dockerfile for pynomo
    FROM debian:stable

    # Install required packages:
    # python, pyx, pip, numpy, scipy, pynomo and their requirements
    RUN apt-get update
    RUN apt-get -y upgrade
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apt-utils
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-pip
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-numpy
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-scipy
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-pyx=0.12.1-11

    RUN DEBIAN_FRONTEND=noninteractive pip install pynomo six

    # Add /app directory and make it working dir
    RUN mkdir -p /app
    ADD . /app
    WORKDIR /app

    CMD ["bash"]


Docker container (environment) `my_pynomo_docker` is built in the directory `/my_directory_path` that has the file `Dockerfile` with command

.. code-block:: bash

    $ docker build -t my_pynomo_docker .

Once environment is built and `my_pynomo_file.py is in directory `/my_directory_path/pdf_py_dir/` one can run

.. code-block:: bash

    $ docker run -it --mount type=bind,source="$(pwd)"/source,target=/app my_pynomo_docker

that opens terminal in `/app directory` of container that is mapped to directory `"$(pwd)"/source` of the host system.
Note the command `$(pwd)` used `pwd` command to print out current working directory.
Inside the container one can run own scripts like:

.. code-block:: bash

    $ python3 my_script.py

That way a folder is used to share the script file and the generated pdf file between host system and the container (virtualized
Linux environment).