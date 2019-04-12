from django.core.management import call_command
from django.test import TestCase


class ClearCache(TestCase):

    @staticmethod
    def test_compilepyc():
        call_command('compilepyc', 'django_pyc', verbosity=1, force=True)

    @staticmethod
    def test_clearpyc():
        call_command('clearpyc', verbosity=1, force=True)
