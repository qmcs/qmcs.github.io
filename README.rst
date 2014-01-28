Python Club at Queen Mary, University of London
===============================================


This is the content of the website of the Python club at Queen Mary,
University of London. You are welcome to contribute your articles.

Getting started
---------------

First of all, get an account at `github <https://github.com>`_, `set up your
ssh key <https://help.github.com/articles/generating-ssh-keys>`_, and `fork
<https://help.github.com/articles/fork-a-repo>`_ the `original repo
<https://github.com/pyclub/pyclub.github.io>`_.

Before writing the code, clone the repo::

    git clone git@github.com:YOUR_USERNAME/pyclub.github.io

create a virtualenv::

    virtualenv .env
    source .env/bin/activate

install needed software::

    pip install -r requirements.txt

now, you are ready to write an article.

Write an article
----------------

Once you have a copy of the repo on your computer you are ready to add
articles to it.

Just create a file in the ``content/articles/`` folder, for example,
``content/articles/001-intro.rst``. Follow the convention: first goes the
number of the article (pick the next integer) followed by a short indicative
name. The content of the file should be similar to

.. code-block:: rst

    .. The title

    Welcome to the QM Python club
    =============================

    .. Some metadata

    :date: 2014-01-28 19:49
    :tags: thats, awesome
    :category: yeah
    :author: Dmitrijs Milajevs

    .. Here goes the context of the article.

    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum.

Refer to `Pelican documentation <http://docs.getpelican.com/en/3.3.0/>`_ and
`reStructuredText examples
<http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_.

Tips
----

You can use `restview <https://pypi.python.org/pypi/restview>`_ to see
rendered ``.rst`` files in your browser.


License
-------

.. image:: http://i.creativecommons.org/l/by/4.0/80x15.png

This work is licensed under a `Creative Commons Attribution 4.0 International
License <http://creativecommons.org/licenses/by/4.0/deed.en_US>`_.
