Commands
========

clearpyc
--------

Clears .pyc files from the project.

.. program:: clearpyc

.. option:: --noinput

    Do NOT prompt the user for input of any kind.

.. option:: -f, --force

    Force the removing files without user interaction.

.. option:: -p, --with-pythonpath

    Remove also PYTHONPATH libraries.

.. option:: path

    Directories with libraries

Example
^^^^^^^

Run command for ``application`` directory only, without prompts and list
processed files:

.. code:: sh

  ./manage.py clearpyc --noinput --verbosity 2 application

compilepyc
----------

Compiles .pyc files in the project.

.. program:: compilepyc

.. option:: -f, --force

    Force the compiling files even if timestamps are up-to-date.

.. option:: -p, --with-pythonpath

    Compile also PYTHONPATH libraries.

.. option:: path

    Directories with libraries

Example
^^^^^^^

Run command Run command for ``application`` directory only and list processed
files:

.. code:: sh

  ./manage.py compilepyc --verbosity 2 application
