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

First, I `covered`__ `Zipf's law <http://en.wikipedia.org/wiki/Zipf%27s_law>`_
and showed that it holds for an English text. As a homework, I asked whether the
same behavior is observed in other languages and what the differences are.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#english-word-frequencies

I could not resist and presented my `research area`__ :) by extracting co-
occurrence counts and projecting the word vectors to 2 dimensions. I managed to
get a plot where ``girl`` is close to ``boy`` but far to ``manager``.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#distributional-semantics

Sprint
------

`@_spyreto_ <https://twitter.com/_spyreto_>`_ and
`Sjoerd de Haan <https://www.linkedin.com/profile/view?id=22830170>`_ liked the
idea of counting word frequencies among various languages and see the behavior
of the slope.

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