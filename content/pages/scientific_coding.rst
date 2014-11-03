==========================
Scientific coding workshop
==========================

:date: 2014-10-07 12:49

The idea is to organize a series of meeting and get familiar with modern
scientific libraries and tools. In the beginning we can go trough `the materials
provided by Software Carpentry`__.

__ http://software-carpentry.org/lessons.html

Once we get familiar with basic topics (for example, array operations, storage,
plotting). We can have a look to specific problems from linguistics, biology,
physics or any other field.

Anyone interested in the subject is very welcome to come! Please contact
Dmitrijs Milajevs <d.milajevs@qmul.ac.uk> if you have any question.

Third meeting: Biggish data processing
======================================

:host: `Dmitrijs (Dima) Milajevs <d.milajevs@qmul.ac.uk>`_
:difficulty: easy
:download: `co-occurrence.ipynb <{filename}/static/notebooks/co-occurrence.ipynb>`_
:show: `notebook <http://nbviewer.ipython.org/url/eecs.io/static/notebooks/co-occurrence.ipynb>`_


Word similarity is the core notion in `distributional semantics`_, where word
meaning is represented as vectors. In such a vector space word similarity is
modeled as the distance between two vectors. There are many datasets to evaluate distributional models, for example, `SimLex-999`_.

During this meeting, we will build our own semantic vector space for the words
in SimLex-999 and measure correlation of model similarity scores with human
judgments using generators and Pandas.

.. _`distributional semantics`: http://en.wikipedia.org/wiki/Distributional_semantics
.. _`SimLex-999`: http://arxiv.org/abs/1408.3456

Second meeting: Estimate n-gram probabilities from a text corpus
================================================================

:host: `Dmitrijs (Dima) Milajevs <d.milajevs@qmul.ac.uk>`_
:difficulty: easy
:download: `n-grams.ipynb <{filename}/static/notebooks/n-grams.ipynb>`_
:show: `notebook <http://nbviewer.ipython.org/url/eecs.io/static/notebooks/n-grams.ipynb>`_

After the `first meeting of the NLP seminar <http://www.eecs.qmul.ac.uk/~dm303/pages/nlp-seminar.html#introduction-to-n-gram-models-oct-6>`_ there was an idea to replicate Table 6.3 in [statistical-nlp]_.

During this meeting we can estimate the n-gram probabilities using MLE from some
corpus. To make things more interesting (and faster) the n-grams counts can be
stored as `Pandas DataFrames`__.

__ http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe

You need to install Pandas to be able to run the code, or you can use
`Wakari <https://www.wakari.io/>`_, a IPython Notebook a cloud.

.. [statistical-nlp] Manning, Christopher D. "Foundations of statistical natural language processing". Ed. Hinrich Schütze. MIT press, 1999.


First meeting: Analyzing Patient Data with Python
=================================================

:host: `Dmitrijs (Dima) Milajevs <d.milajevs@qmul.ac.uk>`_
:difficulty: easy

Follow the Software Carpentry lesson `Analyzing Patient Data`__. The tutorial
goes trough basic data analysis steps: read the data, process it and present
(plot) the result. In addition to the tutorial, we can have a look into `IPython
Notebook`_.

__ http://software-carpentry.org/v5/novice/python/01-numpy.html
.. _`Ipython Notebook`: http://ipython.org/notebook.html

Please `install Python and NumPy <http://software-carpentry.org/v5/setup.html>`_
before the meeting! It might be tricky to get the packages, contact Dima, if you
have any problems. You need to have Anaconda installed, ignore instructions
about the text editor and everything else. After a successful install you should
be able to do the following in a terminal (the version numbers are not that
important):

.. code-block:: bash

    ipython  # or iPython on ipython-2.7
    Python 2.7.8 (default, Oct  3 2014, 02:34:26)
    Type "copyright", "credits" or "license" for more information.

    IPython 2.3.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: import numpy
    In [2]: quit()

Useful links
============

* http://software-carpentry.org/lessons.html
* http://scipy-lectures.github.io
* McKinney, Wes. Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. "O'Reilly Media, Inc.", 2012.
