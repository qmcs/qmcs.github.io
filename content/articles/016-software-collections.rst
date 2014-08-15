====================
Software collections
====================

:date: 2014-08-15 20:49
:tags: scl, deployment
:category: devop
:author: Dmitrijs Milajevs

Intro
=====

.. a couple of sentences introducing the problems software collections are
.. supposed to solve.

Installing software provided in a software collection
=====================================================

In a virtual machine::

    vagrant init chef/centos-6.5
    vagrant ssh

Update the system and enable EPEL::

    sudo yum update
    sudo yum install http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm

Enable Python33 software collection from http://softwarecollections.org::

    sudo yum install https://www.softwarecollections.org/en/scls/rhscl/python33/epel-6-x86_64/download/rhscl-python33-epel-6-x86_64-1-2.noarch.rpm

.. note:: ``rhscl/python33`` versus ``python33`` provied by CentOS.

    CentOS provides a `set of collections`__ that are renamed similarly to the
    collections listed at softwarecollections.org, but (at least at the moment
    of writing) with less packages.

    __ http://wiki.centos.org/AdditionalResources/Repositories/SCL

    It is important to install ``rhscl-python33-epel-6-x86_64-1-2.noarch.rpm``
    instead of ``yum install centos-release-SCL``.

Browse available versions::

    yum list available | grep rhscl

Install a package from a collection::

    sudo yum install python33-numpy

Try it out::

    scl enable python33 bash
    python -c 'import numpy; print(numpy.__file__)'
    /opt/rh/python33/root/usr/lib64/python3.3/site-packages/numpy/__init__.py
    exit

centpkg
=======

Install `centpkg`__, a tool for compiling packages locally from a ``.spec`` file::

    sudo yum install pyrpkg python-setuptools
    git clone  https://git.centos.org/git/centpkg.git
    cd centpkg
    sudo python setup.py install
    cd ..

__ https://git.centos.org/summary/centpkg.git

Install build dependencies needed in the future::

    sudo yum install python33-build scl-utils-build


Build an already existing package using centpkg: NumPy
======================================================

.. note:: This is just an example of how RPMS provided by CentOS can be built.

    ``rhscl/python33`` already provides NumPy, there is no need in building it. Maybe
    only to bump the package version to 1.8.

::

    centpkg clone --anonymous -b c7 python33-numpy
    cd python33-numpy

    sudo yum-builddep SPECS/numpy.spec
    centpkg local

A custom package: versiontools
==============================

Follow this `guide`__.

__ https://access.redhat.com/documentation/en-US/Red_Hat_Developer_Toolset/2/html-single/Software_Collections_Guide/index.html#sect-Extending_the_python27_and_python33_Software_Collections

Another custom package: numexpr
===============================

.. http://data.gpo.zugaina.org/progress/dev-python/numexpr/numexpr-2.4-r1000.ebuild
   doesn't look bad :)

.. Can http://pkgs.fedoraproject.org/cgit/python-numexpr.git/tree/python-numexpr.spec?h=f19 be used directly?

Create a custom software collection. Call it `nlp`.

::

  mkdir -p nlp/SOURCES nlp/SPEC
  cd nlp
  emacs SPEC/nlp.spec

Define a ``numexpr.spec`` file.


.. rpmbuild --define "_topdir \`pwd\`" ...
