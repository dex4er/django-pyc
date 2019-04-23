#!/bin/sh

set -e
set -x

pip install pipenv
pipenv install --dev
pipenv run pip install Django==${DJANGO_VERSION}.*
if [ "$TEST_LINT" = yes ]; then
    pipenv run pip install -r dev-requirements.txt;
else
    pipenv run pip install -r requirements.txt docutils Pygments;
fi
