=======================
Basic git configuration
=======================

:date: 2014-03-04 17:50
:tags: git
:category: coding
:author: Dmitrijs Milajevs

Git is a powerful tool, though it has to be configured first.

-- PELICAN_END_SUMMARY --

Here is a basic ``~/.gitconfig`` file that sets you name, sets up aliases and
enables highlighting in git output:

.. code-block:: ini

    [user]
        name = Dmitrijs Milajevs
        email = dimazest@gmail.com
    [color]
        diff = auto
        status = auto
        branch = auto
        ui = auto
        decorate = short
    [alias]
        st = status
        ci = commit
        br = branch
        co = checkout
        unstage = reset HEAD --
        last = log -1 HEAD

Now you can type ``git st`` instead of ``git status``.