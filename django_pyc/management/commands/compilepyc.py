from optparse import make_option
from django.core.management.base import BaseCommand

import compileall
import os
import sys


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
        for dir in dirs:
            if os.path.isdir(dir) and os.access(dir, os.W_OK):
                for dirname, dirnames, filenames in os.walk(dir):  # @UnusedVariable
                    for filename in filenames:
                        fullname = os.path.join(dirname, filename)
                        compileall.compile_file(fullname, quiet=quiet)
            else:
                if int(options['verbosity']) >= 2:
                    print 'Skipped', dir
