===========================================
Python environment for scientific computing
===========================================

:date: 2015-03-10 10:07
:tags: python
:category: coding
:author: Dmitrijs Milajevs

`Miniconda <http://conda.pydata.org/miniconda.html>`_ is a great way to get
working Python environment on variety of operating systems. This tutorial goes
trough the necessary steps to get a Python environment with common scientific
packages.

Check out `Steve Holden's video <http://holdenweb.blogspot.co.uk/2015/02/how-to-
get-bits-of-python-you-need.html>`_ going trough the same process and his
valuable comments of what's going on.

Install miniconda
=================

Grab miniconda for your platform from the `project page
<http://conda.pydata.org/miniconda.html>`_.

On Mac OS X or Linux:

.. code-block:: bash

    # Download a package for my platform (MacOS X)
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

    # Make it executable
    chmod +x Miniconda3-latest-MacOSX-x86_64.sh

    # Run the installer
    ./Miniconda3-latest-MacOSX-x86_64.sh
    # Press ENTER to see license agreement.
    # (Read it) and press `q` to continue
    # Accept it by typing `yes`.
    # Note the installation prefix (/Users/dimazest/miniconda3).
    # I've decided *not* to add miniconda install location to my PATH
    # (to keep it tidy and avoid confusion).

On Windows, download a corresponding installer from
http://conda.pydata.org/miniconda.html and run it. It's fine to add Python to
your path on Windows, because the OS doesn't provide it's own Python
installation.

Prepare Python environments
===========================

We might get an outdated version, so it's a good idea to update the installation.

Mac OS X or Linux:

.. code-block:: bash

    ~/miniconda3/bin/conda update conda

Windows:

.. code-block:: bash

    conda update conda

As you noticed, you need to prefix ``conda`` with ``~/miniconda3/bin/`` because
it's not in the path on Mac OS X or Linux.

Create Python environments
==========================

Now we are ready to make an environment. It's a good practice to keep a
dedicated environment per project. Imagine you have to projects, one is a web
project and another is a scientific library. The scientific library doesn't need
to the web stack your web application requires and vice-versa. Also this
prevents versioning conflicts. When one project requires an old version of a
library, and another requires the newest version of the same library.

These commands create tow virtual environments called `py34` and `py27` with a
specific Python version and the packages included in `anaconda
<http://docs.continuum.io/anaconda/pkg-docs.html>`_. The environment names are
not the best, but they are fine for the demonstration purposes. Prefer to name
environments after the projects they are created for. Prefer to use Python 3,
because it's the current version of Python. Use Python 2 only if you have to
deal with `software <https://caniusepython3.com/>`_ that is `not compatible with
Python 3 <http://py3readiness.org/>`_.

.. code-block:: bash

    ~/miniconda3/bin/conda create -n py34 anaconda python=3.4  # Python 3.4
    ~/miniconda3/bin/conda create -n py27 anaconda python=2.7  # Optionally, Python 2.7


Activate one of them:

.. code-block:: bash

    # Mac or Linux
    source ~/miniconda3/bin/activate py34
    # Windows
    activate py34

Now you are ready to run `IPython Notebook <http://ipython.org/notebook.html>`_:

.. code-block:: bash

  ipython notebook