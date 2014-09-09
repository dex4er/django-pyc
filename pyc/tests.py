from django.core.management import call_command
from django.test import TestCase


class ClearCache(TestCase):

    def test_compilepyc(self):
        call_command('compilepyc')

    def test_clearpyc(self):
        call_command('clearpyc')
