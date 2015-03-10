===========================================
Python environment for scientific computing
===========================================

:date: 2014-11-18 12:43
:tags: python
:category: coding
:author: Dmitrijs Milajevs

http://conda.pydata.org/miniconda.html

Install miniconda
=================

* Mac OS X or Linux

  .. code-block:: bash

      # Download a package for my platform (MacOS X)
      wget http://repo.continuum.io/miniconda/Miniconda3-3.7.0-MacOSX-x86_64.sh

      # Make it executable
      chmod +x Miniconda3-3.7.0-MacOSX-x86_64.sh

      # Run the installer
      ./Miniconda3-3.7.0-MacOSX-x86_64.sh
      # Press ENTER to see license agreement.
      # (Read it) and press `q` to continue
      # Accept it by typing `yes`.
      # Note the installation prefix (/Users/dimazest/miniconda3).
      # I've decided *not* to add miniconda install location to my PATH
      # (to keep it tidy and avoid confusion).

* On Windows, download a corresponding installer from
  http://conda.pydata.org/miniconda.html and run it.


Prepare Python environments
===========================

Update conda:

* Mac OS X or Linux

  .. code-block:: bash

      ~/miniconda3/bin/conda update conda

* Windows

  .. code-block:: bash

      conda update conda

As you noticed, you need to prefix ``conda`` with ``~/miniconda3/bin/``
because it's not in the path on Mac OS X or Linux.

Create Python environments:

.. code-block:: bash

    conda create -n py34 anaconda python=3.4  # Python 3.4
    conda create -n py27 anaconda python=2.7  # Optionally, Python 2.7


Activate one of them:

.. code-block:: bash

    # Mac or Linux
    source ~/miniconda3/bin/activate py34
    # Windows
    source activate py34
