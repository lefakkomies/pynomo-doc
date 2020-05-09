Python 3 Docker installation
============================

`Docker <https://www.docker.com/>`_ is a platform to create a sandboxed virtualized environments. In the following example `Dockerfile` a virtualized
`Ubuntu <http://ubuntu.com/>`_ is created that has pyNomo installed with all requirements::


    FROM python:3.7-slim-buster

    # Install required packages
    RUN apt-get update && apt-get -y install -y \
        python3 \
        python3-pip \
        texlive-latex-base \
        texlive-fonts-recommended
    RUN DEBIAN_FRONTEND=noninteractive pip3 install pyx pynomo numpy scipy six

    # Add our python app code to the image
    RUN mkdir -p /app
    ADD . /app
    WORKDIR /app

    CMD ["bash"]

    # run command on command line for mapping directory ./source in current directory to folder /app in container
    #
    # docker run -it --mount type=bind,source="$(pwd)"/source,target=/app my_pynomo_docker

Docker container (environment) `my_pynomo_docker` is built in the directory `/my_directory_path` that has the file `Dockerfile` with command

.. code-block:: bash

    $ docker build -t my_pynomo_docker .

Once environment is built and `my_pynomo_file.py is in directory `/my_directory_path/pdf_py_dir/` one can run

.. code-block:: bash

    $ docker run -it -v /my_directory_path/pdf_py_dir:/app my_pynomo_docker

that opens terminal in `/app directory` of container that is mapped to directory `/my_directory_path/pdf_py_dir` of the host system.
There one can run own scripts like:

.. code-block:: bash

    $ python3 my_script.py

That way a folder is used to share the script file and the generated pdf file between host system and the container (virtualized
Linux environment).