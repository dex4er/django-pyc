#!/bin/sh

set -e
set -x

if [ "$TEST_LINT" = yes ]; then
    pipenv run flake8;
    pipenv run pylint --rcfile=setup.cfg django_pyc test_project *.py;
    pipenv run bandit --ini setup.cfg --recursive --format screen .;
    pipenv run doc8 *.rst;
    pipenv run python setup.py build_sphinx;
fi
pipenv run python manage.py test
pipenv run python setup.py check
pipenv run python setup.py sdist bdist_egg bdist_wheel
pipenv run pip install dist/*.whl
