import compileall
from optparse import make_option
import os
import sys

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = \
    """
    Compiles .pyc files in the project.
    """

    option_list = BaseCommand.option_list + (
        make_option('-p', '--with-pythonpath', action="store_true", default=False, dest='with_pythonpath', help='Compile also PYTHONPATH libraries.'),
    )

    def handle(self, **options):
        quiet = 1 if int(options['verbosity']) < 2 else 0
        dirs = sys.path if options['with_pythonpath'] else sys.path[:1]
        for d in dirs:
            if os.path.isdir(d) and os.access(d, os.W_OK):
                for dirname, dirnames, filenames in os.walk(d):  # @UnusedVariable
                    for filename in filenames:
                        fullname = os.path.join(dirname, filename)
                        compileall.compile_file(fullname, quiet=quiet)
            else:
                if int(options['verbosity']) >= 2:
                    print('Skipped', d)
