===========================================
Python environment for scientific computing
===========================================

:date: 2014-11-06 17:00
:tags: python
:category: coding
:author: Dmitrijs Milajevs

http://conda.pydata.org/miniconda.html

Install the package

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
    # I've decided *not* to add miniconda install location to my PATH (to keep it tidy).

Update it

.. code-block:: bash

    ~/miniconda3/bin/conda update conda


Libraries

.. code-block:: bash

    ~/miniconda3/bin/conda install pandas scikit-learn ipython gensim

Simple testing

..code block:: python

    ~/miniconda3/bin/python

    >>> import numpy
    >>> import numpy as np
    >>> np.array([1, 2, 3]) + np.array([10, 20, 30])
    array([11, 22, 33])
