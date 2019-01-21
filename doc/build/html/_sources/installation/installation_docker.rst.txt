Python 2.7.x Docker installation
================================

`Docker <https://www.docker.com/>`_ is a platform to create a sandboxed virtualized environments. In the following example `Dockerfile` a virtualized
`Ubuntu <http://ubuntu.com/>`_ is created that has pyNomo installed with all requirements::

    FROM ubuntu

    # Install required packages:
    # python, pyx, pip, numpy, scipy, pynomo and their requirements
    RUN apt-get update
    RUN apt-get -y upgrade
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-pyx
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-pip
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-numpy
    RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python-scipy
    RUN DEBIAN_FRONTEND=noninteractive pip install pynomo

    # Add /app directory and make it working dir
    RUN mkdir -p /app
    ADD . /app
    WORKDIR /app

    # Set the default command to execute -> "python my_pynomo_file.py"
    CMD ["python", "my_pynomo_file.py"]

Docker container (environment) `my_pynomo_docker` is built in the directory `/my_directory_path` that has the file `Dockerfile` with command

.. code-block:: bash

    $ docker build -t my_pynomo_docker .

Once environment is built and `my_pynomo_file.py is in directory `/my_directory_path/pdf_py_dir/` one can run

.. code-block:: bash

    $ docker run -i -v /my_directory_path/pdf_py_dir:/app my_pynomo_docker

that runs command ``python my_pynomo_file.py`` inside `/app directory` of container that is mapped to directory `/my_directory_path/pdf_py_dir` of the host system.
That way a folder is used to share the script file and the generated pdf file between host system and the container (virtualized
Linux environment).