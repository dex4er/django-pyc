import sys

from optparse import make_option
from django.core.management import call_command
from django.core.management.base import BaseCommand

# stop the project from compiling bytecode when running clean command.
sys.dont_write_bytecode = True

class Command(BaseCommand):
    """
    Manages *.pyc files in the project.
    """

    help = \
    """
    Manages *.pyc files in the project.
    """

    option_list = BaseCommand.option_list  + (
        make_option('-f', '--force', action="store_true", default=False, dest='force', help='Force the cleanup without user interaction.'),
    )

    def handle(self, force, **kwargs):
        self.stdout.write("TODO compilepyc command.")
