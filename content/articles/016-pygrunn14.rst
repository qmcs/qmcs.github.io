Pygrunn 2014
============

:date: 2014-05-10 15:56
:tags: conference, talk, nlp, pygrunn
:category: life
:author: Dmitrijs Milajevs
:template: article_cover
:cover: 016-pygrunn14.jpg

`Pygrunn <http://www.pygrunn.org/>`_ is an awesome conference for Python
developers and friends, which takes place in
`Groningen <http://en.wikipedia.org/wiki/Groningen>`_.

As usually, the conference was perfectly organized. This is one of the most
stylish conferences I've ever attended. It constantly grows, and next year the
conference moves to a bigger venue, so keep the beginning of May 2015 free and
attend the event.

Another positive trend is the growing proportion of science related talks. One
of the topics of the conference became (scientific) code quality and
collaboration between professional developers and scientists.

Check awesome summaries of talks by
`Reinout van Rees <http://reinout.vanrees.org/weblog/tags/pygrunn.html>`_
and
`Maurits van Rees <http://maurits.vanrees.org/weblog/topics/pygrunn>`_. Get the
`#pygrunn <https://twitter.com/search?q=%23PyGrunn>`_ tweets and follow
`@pygrunn <https://twitter.com/PyGrunn>`_.


Computational linguistics 101
-----------------------------

`My presentation`__ started as a demonstration of the modern pythonic scientific
tools (my subjective classification):

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb

1. Data structures
    * `numpy <http://www.numpy.org/>`_
    * `scipy <http://www.scipy.org/scipylib/index.html>`_
    * `pandas <http://pandas.pydata.org/>`_
2. Algorithms
    * `scikit-learn <http://scikit-learn.org/>`_
    * `nltk <http://www.nltk.org/>`_,
    * `textblob <http://textblob.readthedocs.org>`_
    * `gensim <http://radimrehurek.com/gensim/>`_
3. Reporting
    * `ipython <http://ipython.org/>`__
    * `matplotlib <http://matplotlib.org/), [seaborn](http://www.stanford.edu/~mwaskom/software/seaborn/>`__

However, I find the technical talks with a lot of code rather boring, so I
decided to show how these libraries are used to solve simple CL tasks.

A universal pattern behind natural languages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, I `covered`__ `Zipf's law <http://en.wikipedia.org/wiki/Zipf%27s_law>`_,
which states that the frequency of any word in a corpus of texts is inversely
proportional to its rank in the frequency table. To show that the law holds for
an English text, I loaded `the BNC frequency list`__ provided by `Adam
Kilgarriff`__ into `Pandas <http://pandas.pydata.org/>`_ `DataFrame`__ and
plotted the sorted frequencies on the log-log scale.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#english-word-frequencies
__ http://www.kilgarriff.co.uk/BNClists/lemma.num
__ http://www.kilgarriff.co.uk/bnc-readme.html
__ http://pandas.pydata.org/pandas-docs/version/0.13.1/generated/pandas.DataFrame.html

.. image:: {filename}/static/images/016-bnc_freq.png
    :align: center
    :alt: English word frequency counts extracted from the British National Corpus on the log-log scale.
    :target: {filename}/static/images/016-bnc_freq.png

As a homework, I asked whether the same behavior is observed in
other languages and what the differences are.

Distributional semantics
~~~~~~~~~~~~~~~~~~~~~~~~

I could not resist and `presented`__ my `research area`__ :) by extracting word
co-occurrence counts and projecting the word vectors to 2 dimensions using
`scikit-learn`__ implementation of `manifold learning`__.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#distributional-semantics
__ http://www.eecs.qmul.ac.uk/~dm303/
__ http://scikit-learn.org/stable/
__ http://scikit-learn.org/stable/modules/manifold.html

In distributional semantics, words are represented as rows in a matrix. The
columns correspond to other words the word co-occurs with. The values of the
matrix are the frequencies the words co-occurred together. For example, here are
the vectors for the words ``idea``, ``notion``, ``boy`` and ``girl``.

======= ========== ==== ======
\       philosophy book school
======= ========== ==== ======
idea    10         47   39
notion  7          3    15
boy     0          12   146
girl    0          19   93
======= ========== ==== ======

So, ``idea`` was seen with ``philosophy`` 10 times in the corpus I used. An
occurrence in this case means that ``philosophy`` was not more than 5 words
further from ``idea``.

The number patterns for ``boy`` and ``girl`` are much more similar than for
``boy`` and ``notion``, suggesting that ``boy`` is much more similar to ``girl``
than to ``notion``.

.. image:: {filename}/static/images/016-ds.png
    :align: center
    :alt: Word semantic relatedness.
    :target: {filename}/static/images/016-ds.png

I used manifold learning to provide a visualization for a bigger set of words
(and a much bigger set of contexts).

Sprint
------

`@_spyreto_ <https://twitter.com/_spyreto_>`_ and
`Sjoerd de Haan <https://www.linkedin.com/profile/view?id=22830170>`_ liked the
idea of counting word frequencies among various languages and see how they
compare in relation to Zipf's law.

Initially, we wanted to take EU directives and compare the official EU languages,
however, the website was down, and we were kindly redirected to
`this page <http://sorry.ec.europa.eu/>`_ every time we wanted to get a legal
document.

Luckily, we found an already prepared `word frequencies for a many languages
<http://invokeit.wordpress.com/frequency-word-lists/>`_ and reused them.

The task was to

* plot the ranked frequency distribution on the log-log scale
* estimate the slope :math:`\alpha`, the ratio of the frequencies between the
  neighboring words in the rank.

`We tried`__ English, Dutch, Russian, Latvian, Spanish and Italian. All languages
obey Zipf's law, at least visually. Here is a plot for English (see `the notebook`__
for other plots):

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/Word%20frequencies.ipynb
__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/Word%20frequencies.ipynb

.. image:: {filename}/static/images/016-en_zipf.png
    :align: center
    :alt: English word frequency counts on the log-log scale.
    :target: {filename}/static/images/016-en_zipf.png

The blue line is the provided frequencies, the green is a regression line.
Theory [Li1992]_ says that the slope coefficient should be close to -1. As the
table shows, the values deviate from -1 quite drastically (-1.7 for Spanish).
Also, the `slope estimate`__ for English from the `British National Corpus`__ is
-1.18.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#estimating-the-slope
__ http://www.natcorp.ox.ac.uk/

=========  ========= ===========
Language   Slope     Intercept
=========  ========= ===========
uk         -1.044263 11.212273
nl         -1.566664 19.635268
ru         -1.395736 17.781756
lv         -1.055992 11.541761
es         -1.707326 22.161790
it         -1.601567 20.000540
=========  ========= ===========

Conclusion
----------

.. [Li1992] Li, Wentian.
            `Random texts exhibit Zipf's-law-like word frequency distribution.`__
            Information Theory, IEEE Transactions on 38.6 (1992): 1842-1845.

__ http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.164.8422&rep=rep1&type=pdf