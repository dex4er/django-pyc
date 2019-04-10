.. image:: https://img.shields.io/pypi/v/django-pyc.png
   :target: https://pypi.python.org/pypi/django-pyc
.. image:: https://travis-ci.org/dex4er/django-pyc.png?branch=master
   :target: https://travis-ci.org/dex4er/django-pyc
.. image:: https://readthedocs.org/projects/django-pyc/badge/?version=latest
   :target: http://django-pyc.readthedocs.org/en/latest/
.. image:: https://img.shields.io/pypi/pyversions/django-pyc.svg
   :target: https://www.python.org/
.. image:: https://img.shields.io/pypi/djversions/django-pyc.svg
   :target: https://www.djangoproject.com/

django-pyc
==========

django-pyc is a package that implements additional commands for Django's
``manage.py`` command.

django-pyc allows to remove or recompile all ``.pyc`` files in the project or
Python libraries.


Installation
------------

Install with ``pip`` or ``pipenv``:

.. code:: python

  pip install django-pyc

Add ``django_pyc`` to your installed apps in your settings.py file:

.. code:: python

  INSTALLED_APPS = [
      'django_pyc',
      ...
  ]


Commands
--------

clearpyc
^^^^^^^^

Clears .pyc files from the project.

Options:

``--noinput``
  Do NOT prompt the user for input of any kind.

``-f``, ``--force``
  Force the removing files without user interaction.

``-p``, ``--with-pythonpath``
  Remove also PYTHONPATH libraries.

``path``
  Directories with libraries

Example:

Run command for ``application`` directory only, without prompts and list
processed files:

.. code:: sh

  ./manage.py clearpyc --noinput --verbosity 2 application

compilepyc
^^^^^^^^^^

Compiles .pyc files in the project.

Options:

``-f``, ``--force``
  Force the compiling files even if timestamps are up-to-date.

``-p``, ``--with-pythonpath``
  Compile also PYTHONPATH libraries.

``path``
  Directories with libraries

Example:

Run command Run command for ``application`` directory only and list processed
files:

.. code:: sh

  ./manage.py compilepyc --verbosity 2 application


Documentation
-------------

See http://django-pyc.readthedocs.org/


License
-------

Copyright © 2014, 2019, Piotr Roszatycki

This software is distributed under the GNU Lesser General Public License (LGPL
3 or greater).
