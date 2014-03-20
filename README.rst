Python Club at Queen Mary, University of London
===============================================


This is the content of the `website of the Python club at Queen Mary,
University of London <http://pyclub.github.io/>`_. You are welcome to
contribute your articles on any more or less technical topics, not necessarily
related to Python (for instance, if you know a bit about port forwarding using
``ssh``, and able to f*ck the system and pretend that the school SQL server is
running locally, write it here).

Getting started
---------------

First of all, get an account at `github <https://github.com>`_, `set up your
ssh key <https://help.github.com/articles/generating-ssh-keys>`_, and `fork
<https://help.github.com/articles/fork-a-repo>`_ the `original repo
<https://github.com/pyclub/pyclub.github.io>`_. Right, you also need to
`configure git <https://help.github.com/articles/set- up-git>`_. If you didn't
use git before, check out `Github tutorial <http://try.github.io>`_ or a
`tutorial provided by Software Carpentry
<http://apawlik.github.io/2014-02-03-TGAC/lessons/tgac/version-
control/tutorial.html>`_ to get a general idea.


Before writing an article, clone the repo::

    git clone git@github.com:username/pyclub.github.io
    cd pyclub.github.io

We use `buildout <https://pypi.python.org/pypi/zc.buildout/2.2.1>`_ to deploy
needed software. A typical biuldout deployment consists of two steps:
bootstrapping and building out.

Bootstraping is simple::

    python bootstrap.py

In case you get an error about setuptools, you can install them::

    # Only if you get an error in the previus step!
    python ez_setup.py --user
    python bootstrap.py

Now you are ready to buildout::

    bin/buildout


Writing an article
------------------

Once you have a copy of the repo on your computer you are ready to add
articles to it.

Just create a file in the ``content/articles/`` folder, for example,
``content/articles/001-intro.rst``. Follow the convention: first goes the
number of the article (pick the next integer) followed by a short indicative
name. The content of the file should be similar to

.. code-block:: rst

    .. The title. It's important to put = from below and above!

    =============================
    Welcome to the QM Python club
    =============================

    .. Some metadata

    :date: 2014-01-28 19:49
    :tags: thats, awesome
    :category: yeah
    :author: Dmitrijs Milajevs

    The first paragraph should introduce and possibly summarize the article. It
    should be relatively short: 2 - 3 sentences.

    .. Explicitly mark the end of the summary/introduciton

    -- PELICAN_END_SUMMARY --

    .. Here goes the rest of the article.

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum.

Refer to `Pelican documentation <http://docs.getpelican.com/en/3.3.0/>`_ and
`reStructuredText examples
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_ if you want
nice formatting.

An easy way to see rendered .rst files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use `restview <https://pypi.python.org/pypi/restview>`_ to see
rendered ``.rst`` files in your browser. For example, to see the intro
article, type::

    bin/restview content/articles/001-intro.rst

There are rumors, that you can feed a directory to restview and then select
files in the browser::

    bin/restview content

Generate the HTML version of a blog locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wow, you can get a local version of the blog::

    make devserver
    open http://localhost:8000  # gnome-open on Linux
    # make stopserver is a logical way to stop the server

Share with others
~~~~~~~~~~~~~~~~~

Commit and push our changes::

    git st  # see what you have done
    git diff  # really see what you have done
    git add RELATED_FILES  # probably, somethig like content/articles/001-intro.rst
    git ci -m'An article describing the enterprise (R) power of Java.'
    git push  # send you changes to github

Create a `pull request <https://help.github.com/articles/creating-a-pull-request>`_.

Why should I bother?
--------------------

Sharing your knowledge is cool. You can always put in your CV that you
contribute to a blog, know git, familiar with peer reviews, and able to read
documentation.

You can also directly point to your work. Your next employer will like it.

Updating the web site
---------------------

In case you are lucky and have write access to the main repo you can upload the
generated HTML version of the site, however you need to clone
``git@github.com:pyclub/pyclub.github.io.git``.

To upload the HTML just run::

    make github

License
-------

.. image:: http://i.creativecommons.org/l/by/4.0/80x15.png

This work is licensed under a `Creative Commons Attribution 4.0 International
License <http://creativecommons.org/licenses/by/4.0/deed.en_US>`_.
