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
    * `NumPy <http://www.numpy.org/>`_
    * `SciPy <http://www.scipy.org/scipylib/index.html>`_
    * `Pandas <http://pandas.pydata.org/>`_
2. Algorithms
    * `scikit-learn <http://scikit-learn.org/>`_
    * `NLTK <http://www.nltk.org/>`_,
    * `TextBlob <http://textblob.readthedocs.org>`_
    * `gensim <http://radimrehurek.com/gensim/>`_
3. Reporting
    * `IPython <http://ipython.org/>`__
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

`Spyros Ioakeimidis <https://twitter.com/_spyreto_>`_ and
`Sjoerd de Haan <https://www.linkedin.com/profile/view?id=22830170>`_ liked the
idea of counting word frequencies among various languages and see how they
compare in relation to Zipf's law.

Initially, we wanted to take EU directives and compare the official EU languages,
however, the website was down, and we were kindly redirected to
`this page <http://sorry.ec.europa.eu/>`_ every time we wanted to get a legal
document.

Luckily, we found an already prepared `word frequencies for many languages
<http://invokeit.wordpress.com/frequency-word-lists/>`_ and reused them. We
wrote a simple function to plot the frequency of the words against the rank of
the words in the frequency table. Here is the top 10 most frequently used words
in English, Dutch and Latvian:

==== ======== ========= ======== ========= ======== =========
\    English            Dutch              Latvian
---- ------------------ ------------------ ------------------
Rank Word     Frequency Word     Frequency Word     Frequency
==== ======== ========= ======== ========= ======== =========
1    you      6281002   ik       2091479   ir       20182
2    i        5685306   je       1995150   es       19042
3    the      4768490   het      1428477   un       12737
4    to       3453407   de       1399236   tu       12141
5    a        3048287   is       1202489   tas      8601
6    it       2879962   dat      1188131   ka       7964
7    and      2127187   een      1011496   man      7725
8    that     2030642   niet     997681    to       7535
9    of       1847884   en       774098    vai      7527
10   in       1554103   wat      618627    ko       6906
==== ======== ========= ======== ========= ======== =========

If you plot the word rank on the x axis and the word frequency on the y axis on
a log-log scale you should see a straight line. A straight line on a log-log
plot implies that the quantities on the two axis are related trough a power law.
Thus, if our data would fit straight line perfectly, that would mean that the
frequency of a word occurring is exactly proportional to a power of the rank of
that word in the frequency table. This is the content of Zipf's law, but
of course, such laws are never exact.

.. image:: {filename}/static/images/016-en_zipf.png
    :align: center
    :alt: English word frequency counts on the log-log scale.
    :target: {filename}/static/images/016-en_zipf.png

The blue line is the provided frequencies, the green is a regression line.

One thing we can compare amongst languages is how well this plot follows a
straight line. Also the slope of the line contains interesting information. It
tells what kind of power law we are dealing with exactly.

The slope is related to the morphology of a language. For example, in Latvian,
which has quite rich morphology, the word `"city"` is `"pilsēta"`, but the
English phrase `"in a city"` is `"pilsētā"`. All the occurrences of "`pilsēta`"
in a Latvian text will be distributed over several morphological forms, lowering
the counts. As a result, the slope for a Latvian text will be less steep
comparing to English.

We `tried`__ English, Ukrainian, Dutch, Russian, Latvian, Spanish and Italian. All
languages obey Zipf's law, at least visually.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/Word%20frequencies.ipynb

=========  ========= ===========
Language   Slope     Intercept
=========  ========= ===========
en         -1.717729 21.934904
uk         -1.044263 11.212273
nl         -1.566664 19.635268
ru         -1.395736 17.781756
lv         -1.055992 11.541761
es         -1.707326 22.161790
it         -1.601567 20.000540
=========  ========= ===========

Theory [Li1992]_ says that the slope coefficient should be close to -1. As the
table below shows, the values deviate from -1 quite drastically (-1.57 for
Dutch, for example). Also, the `slope estimate`__ for English from the `British
National Corpus`__ is -1.18 in contrary to -1.72. Here is the Zipf's law
visualization for English extracted from the BNC.

__ http://nbviewer.ipython.org/urls/bitbucket.org/dimazest/phd-buildout/raw/tip/notebooks/pygrunn14.ipynb#estimating-the-slope
__ http://www.natcorp.ox.ac.uk/

.. image:: {filename}/static/images/016-en_bnc_zipf.png
    :align: center
    :alt: Actual and estimated English word frequencies from the BNC.
    :target: {filename}/static/images/016-en_bnc_zipf.png

Conclusion
----------

Pygrunn is a great conference that start attracting not only (professional web)
developers, but also scientists. I was really surprised that my talk got a bit
of attention and people were willing to hack around a linguistic phenomena. I
hope that next year this trend continues. And the two communities become closer
to each other.

.. [Li1992] Li, Wentian.
            `Random texts exhibit Zipf's-law-like word frequency distribution.`__
            Information Theory, IEEE Transactions on 38.6 (1992): 1842-1845.

__ http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.164.8422&rep=rep1&type=pdf