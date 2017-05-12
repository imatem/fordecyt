========
FORDECyT
========

Progarama para un avance global e intregado de la Matemática Mexicana.

.. contents::


Quickstart
----------

.. code-block:: bash

    $ git clone https://github.com/imatem/fordecyt
    $ cd fordecyt

Add a file that contains a passwort. Do **not** use ``admin`` as a password in production!

.. code-block:: bash

    $ echo -e "[buildout]\nlogin = admin\npassword = admin" > secret.cfg

Symlink to the file that best fits you local environment. At first that is usually development. Later you can use production or test. This buildout only uses ``local.cfg`` and ignores all ``profiles/local_*.cfg``.

.. code-block:: bash

    $ ln -s profiles/local_develop.cfg local.cfg

Build Plone

.. code-block:: bash

    $ virtualenv-2.7 --no-site-packages .
    $ ./bin/pip install -r requirements.txt
    $ ./bin/buildout
