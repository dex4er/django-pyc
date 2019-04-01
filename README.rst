.. image:: https://img.shields.io/pypi/v/django-pyc.png
   :target: https://pypi.python.org/pypi/django-pyc
.. image:: https://travis-ci.org/dex4er/django-pyc.png?branch=master
   :target: https://travis-ci.org/dex4er/django-pyc
.. image:: https://readthedocs.org/projects/django-pyc/badge/?version=latest
   :target: http://django-pyc.readthedocs.org/en/latest/

django-pyc
==========

django-pyc is a package that implements additional commands for Django's
``manage.py`` command.

django-pyc allows to remove or recompile all ``.pyc`` files in the project or
Python libraries.


Installation
------------

Add `django_pyc` to your installed apps in your settings.py file.

.. code:: python

  INSTALLED_APPS = [
      'django_pyc',
      ...
  ]


Usage
-----

From your shell, type:

.. code:: sh

  python manage.py clearpyc

or

.. code:: sh

  python manage.py compilepyc

Example
^^^^^^^

Run commands without prompts and with list of processed files:

.. code:: sh

  ./manage.py clearpyc --noinput --verbosity 2 application
  ./manage.py compilepyc --verbosity 2 application
