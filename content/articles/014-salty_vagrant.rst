=====================================
The practical side of reproducibility
=====================================

:date: 2014-04-06 16:12
:tags: vagrant, salt, deployment
:category: reproducibility
:author: Dmitrijs Milajevs

In the `previous post <{filename}/articles/013-cw14.rst>`_ I pointed out some
difficulties of developing a reproducible experiment. Over a weekend, I've
applied some of that ideas to `my paper`__ and would like to share my
experience.

__ http://www.eecs.qmul.ac.uk/~dm303/cvsc14.html

This is the second attempt of making this work reproducible. The first was done
by `Alexander Konovalov`__, `Devasena Inupakutika`__, `Steve Crouch`__ and me at
the `Collaborations Workshop`__. Our aim was to reproduce an experiment and run
it in `Microsoft Azure`_.

.. _Microsoft Azure: http://azure.microsoft.com/

By that time I'd already had a `Vagrant box`__ that contained all the necessary
software. However, Fedora 20, the OS I used, is not supported by Azure, so we
had to use another OS.

__ http://docs.vagrantup.com/v2/boxes.html

Finally, we managed to create a VM image and run the experiment in the cloud.
However, deployment took most of the time, because we had to install the system
dependencies manually. It was a messy list of development libraries and Python
3.3.

__ http://alexk.host.cs.st-andrews.ac.uk
__ http://www.software.ac.uk/about/people/devasena-inupakutika
__ http://www.software.ac.uk/about/people/steve-crouch
__ http://www.software.ac.uk/collaborations-workshop-2014-cw14-software-your-reproducible-research

-- PELICAN_END_SUMMARY --

Automating things
=================

We would spend much less time on deployment if we had an idea what packages we
needed to install. A declarative description of what packages had to be
installed would help us a lot. Luckily, `salt`_,  which nicely `integrates with
Vagrant`__, allows to do exactly this.

.. _salt: https://salt.readthedocs.org/en/latest/
__ http://docs.vagrantup.com/v2/provisioning/salt.html

While vagrant abstracts away all the difficulty and diversity of virtualization
software, salt hides away the quirks of the guest OS. Salt describes the desired
OS configuration as a set of `states`_. A state can be an installed package, a
file or `almost anything else`__. In `my Vagrant setup`__, I got `4 kinds of salt states`__.

.. _states: http://salt.readthedocs.org/en/latest/topics/tutorials/starting_states.html
__ http://salt.readthedocs.org/en/v0.17.5/ref/states/all/index.html
__ https://bitbucket.org/dimazest/phd-buildout/src/722ad58af0e3b8a3987758204b9bc78f46395b30/Vagrantfile
__ https://bitbucket.org/dimazest/phd-buildout/src/722ad58af0e3b8a3987758204b9bc78f46395b30/salt/roots/salt/basic.sls

System packages
---------------

The first class of states describes what system packages have to be installed.
Here is the relevant part of the configuration file:

.. code-block:: jinja

    {% set packages = [
      'atlas-sse3-devel',
      'blas-devel',
      'bzip2-devel',
      'czmq-devel',
      'freetype-devel',
      'gcc-c++',
      'git',
      'hdf5-devel',
      'htop',
      'libpng-devel',
      'libyaml-devel',
      'lzo-devel',
      'mercurial',
      'python3',
      'python3-Cython',
      'python3-devel',
      'python3-matplotlib',
      'python3-numexpr',
      'python3-numpy',
      'python3-PyYAML',
      'python3-scikit-learn',
      'python3-scipy',
      'python3-setuptools',
      'python3-tables',
      'python3-zmq',
      'tmux',
      'unzip',
    ]
    %}

    {% for pkg in packages %}
    {{ pkg }}:
      pkg.installed
    {% endfor %}

Because salt configuration files are `Jinja`_ templates, it is possible to avoid
unnecessary repetition and keep the configuration file clear.

.. _jinja: http://jinja.pocoo.org

System configuration
~~~~~~~~~~~~~~~~~~~~

The second set of packages configures the system and leaves some hints on how to
run the experiments. The ``README`` file lists the commands needed to be run to
execute experiments presented in the paper.

.. code-block:: yaml

    bashrc:
      file.append:
        - name: /home/vagrant/.bashrc
        - text: export LC_ALL="en_US.UTF-8"

    /etc/motd:
      file.append:
        - text: |
            Dialogue act tagging.

            This is an isolated environment to run dialogue act tagging experiments.
            For more details, see http://www.eecs.qmul.ac.uk/~dm303/cvsc14.html

            Check README for further instructions.

    README:
      file.copy:
        - name: /home/vagrant/README
        - source: /srv/home/README
        - force: true

    tmux_conf:
      file.copy:
        - name: /home/vagrant/.tmux.conf
        - source: /srv/home/tmux.conf
        - force: true

Deployment
----------

The deployment states retrieve the custom experiment software and deploy it. In
my setup I use buildout. By the way, the same buildout configuration is used for
development, which guarantees that it's up to date.

.. code-block:: yaml

  tools:
    hg.latest:
      - name: https://dimazest@bitbucket.org/dimazest/phd-buildout
      - target: /home/vagrant/tools
      - rev: tip
      - runas: vagrant

  tools_buildout.cfg:
    file.symlink:
      - name: /home/vagrant/tools/buildout.cfg
      - target: /home/vagrant/tools/_buildout.cfg
      - require:
        - hg: tools

  tools_buildout_bootstrap:
    cmd.run:
      - name: python3.3 bootstrap.py
      - cwd: /home/vagrant/tools
      - user: vagrant
      - unless: ls /home/vagrant/tools/bin/buildout

  buildout:
    cmd.run:
      - name: bin/buildout
      - cwd: /home/vagrant/tools
      - user: vagrant
      - env:
        - LC_ALL: en_US.UTF-8

Data
----

The experiments use several resources. `The Switchboard corpus`__, its typical
training and testing splits and the word vector spaces. All the data is acquired
and put to the right place by salt:

__ http://compprag.christopherpotts.net/swda.html

.. code-block:: yaml

  swda:
    file.managed:
      - name: /home/vagrant/swda.zip
      - source: http://compprag.christopherpotts.net/code-data/swda.zip
      - source_hash: sha512=fb24f4c5be4e69490535951237a41cd320fe53d7fb2782d3624b0bb99da7a4461ad1ee8bbfeb3e22e38e0b706ae377787d437eb9308d6d32bf16481f7dd1f228

  swda_unzip:
    cmd.run:
      - name: yes | unzip swda.zip
      - cwd: /home/vagrant
      - unless:: ls /home/vagrant/swda/

  swda_train_split:
    file.managed:
      - name: /home/vagrant/downloads/switchboard/ws97-train-convs.list.txt
      - source: http://www.eecs.qmul.ac.uk/~dm303/static/papers/cvsc14/ws97-train-convs.list.txt
      - source_hash: sha512=d497e4152afc8e3792cfadd0c52ebafad85aea21b65efc5918189a90dfe4aed2604e3d2b6827343d49425b5985a8eb39a3a4729d1c45e572757b4cecb5341bc0

  swda_test_split:
    file.managed:
      - name: /home/vagrant/downloads/switchboard/ws97-test-convs.list.txt
      - source: http://www.eecs.qmul.ac.uk/~dm303/static/papers/cvsc14/ws97-test-convs.list.txt
      - source_hash: sha512=cb7e53d3471e63d46b12608db0f2b372c99269a2b7cfa6a4e0997cd7e22d518d5e227a19a572b4de2ce0773434ca5e9ee82022cd88408592dfa16492e3fb0f03

  nltk_data:
    cmd.run:
      - name: /home/vagrant/tools/bin/fowler.corpora-py -c "import nltk; nltk.download('all')"
      - creates: /home/vagrant/nltk_data
      - user: vagrant

  cvsc14_space_raw:
    file.managed:
      - name: /home/vagrant/data/matrix_swda_c-google-100_3k.h5
      - source: http://www.eecs.qmul.ac.uk/~dm303/static/papers/cvsc14/matrix_swda_c-google-100_3k.h5
      - source_hash: sha512=c15a9f2d7117305bbcb1b32123e62cfdf0861548d3dc6c2401fd23eeffcb7053c9aa51c16b3ec15236d9aa78385966f92fc5594d77c2ef1066915d20e80d29c4

  cvsc14_space_tf_idf:
    file.managed:
      - name: /home/vagrant/data/matrix_swda_c-google-100_3k_tf-idf-l2.h5
      - source: http://www.eecs.qmul.ac.uk/~dm303/static/papers/cvsc14/matrix_swda_c-google-100_3k_tf-idf-l2.h5
      - source_hash: sha512=153572ed754674337a985a8c6ae140cdab73227e2ba74cddad03d13c9e797c32a164b3e917fca43d05bd0238e7a12dce5c5bd24c0f5aec53ed396c31408b023f

  cvsc14_space_nmf:
    file.managed:
      - name: /home/vagrant/data/matrix_swda_c-google-100_3k_line_normalized_nmf1k.h5
      - source: http://www.eecs.qmul.ac.uk/~dm303/static/papers/cvsc14/matrix_swda_c-google-100_3k_line_normalized_nmf1k.h5
      - source_hash: sha512=ca14e57e5ceed8073d259088644df6847a9c549b1bad61c9df8563da78ca7f1c239f29b6cbac04091aca90d8c135daff48b7eda8c22b48ffb0cf592f60df6eb5

As a nice bonus, the checksums are checked to guarantee that you get the same
data as I.

Meta experiment
===============

Now, the experiment can be rerun in a few steps:

.. code-block:: bash

  $ hg clone https://bitbucket.org/dimazest/phd-buildout
  $ cd phd-buildout
  $ vagrant up  # I had to wait for 48 minutes...
  $ vagrant ssh
  Last login: Sun Apr  6 14:29:55 2014
  Dialogue act tagging.

  This is an isolated environment to run dialogue act tagging experiments.
  For more details, see http://www.eecs.qmul.ac.uk/~dm303/cvsc14.html

  Check README for further instructions.
  [vagrant@localhost ~]$ tools/bin/corpora serafin03 plain-lsa  # A nice opportunity for my laptop's fan to show it's presence :)
  :paper: Serafin et al. 2003
  :accuracy: 0.617
  :command: tools/bin/corpora serafin03 plain-lsa

  ==================== ========== ========== ========== ==========
                   tag  precision     recall   f1-score    support
  ==================== ========== ========== ========== ==========
                     %      0.515      0.694      0.592        360
                    ^2      0.190      0.211      0.200         19
                    ^h      0.200      0.143      0.167          7
                    ^q      0.000      0.000      0.000         17
                    aa      0.515      0.327      0.400        208
               aap\_am      0.000      0.000      0.000          7
                    ad      0.143      0.037      0.059         27
                    ar      0.000      0.000      0.000          3
               arp\_nd      0.000      0.000      0.000          3
                     b      0.764      0.916      0.834        765
                   b^m      0.000      0.000      0.000         21
                    ba      0.529      0.724      0.611         76
                    bd      1.000      1.000      1.000          1
                    bf      0.000      0.000      0.000         23
                    bh      0.480      0.571      0.522         21
                    bk      0.327      0.571      0.416         28
                    br      0.714      0.556      0.625          9
                    fa      0.500      0.500      0.500          2
                    fc      0.660      0.432      0.522         81
  fo\_o\_fw\_"\_by\_bc      0.250      0.062      0.100         16
                    fp      0.333      0.200      0.250          5
                    ft      0.000      0.000      0.000          7
                     h      0.667      0.609      0.636         23
                    na      0.000      0.000      0.000         10
                    ng      0.500      0.167      0.250          6
                    nn      0.479      0.885      0.622         26
                    no      0.000      0.000      0.000          6
                    ny      0.455      0.068      0.119         73
                    qh      0.250      0.083      0.125         12
                    qo      0.524      0.688      0.595         16
                   qrr      0.250      0.500      0.333          2
                    qw      0.594      0.345      0.437         55
                  qw^d      0.000      0.000      0.000          1
                    qy      0.425      0.405      0.415         84
                  qy^d      0.308      0.111      0.163         36
                    sd      0.620      0.790      0.695       1317
                    sv      0.568      0.255      0.352        718
                    t1      0.000      0.000      0.000          1
                     x      0.887      1.000      0.940         94
  -------------------- ---------- ---------- ---------- ----------
    weighted avg/total      0.592      0.617      0.582       4186
  ==================== ========== ========== ========== ==========

  The model is trained on the full development set.
  The scores are computed on the full evaluation set.

Future work
===========

There are several ways to improve the setup.

So far, I've used Fedora 20 as the guest OS. It's possible to configure salt to
`perform different actions for different OS`__. For example, it would be nice to
have support for Ubuntu, or even `Gentoo prefix`__.

__ http://salt.readthedocs.org/en/v0.17.5/topics/tutorials/states_pt3.html#using-grains-in-sls-modules
__ http://www.gentoo.org/proj/en/gentoo-alt/prefix/

Adaptation to another provisioner, for example, `Docker`_ to minimize isolation
overhead would be another great enhancement.

.. _Docker: http://docs.vagrantup.com/v2/provisioning/docker.html

Nicer data management, probably, using `dat`_ would keep the setup clearer.

.. _dat: http://dat-data.com

Finally, it would be nice to deploy the created virtual machine in a cloud and
run all the experiments there. The trick is that some experiments require quite
a lot of RAM and were originally run on a machine with 16 CPUs and 128 GB of
RAM.
