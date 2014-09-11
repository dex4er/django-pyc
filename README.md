django-pyc
==========

django-pyc is a package that implements additional commands for Django's
`manage.py` command.

django-pyc allows to remove or recompile all `.pyc` files in the project
or Python libraries.


Installation
------------

Add `django_pyc` to your installed apps in your settings.py file.

    INSTALLED_APPS = [
        'django_pyc',
        ...
    ]


Usage
-----

From your shell, type:

    python manage.py clearpyc

or

    python manage.py compilepyc
