import argparse
import compileall
import os
import sys

from django.core.management import base


class Command(base.BaseCommand):
    help = \
        """
        Compiles .pyc files in the project.
        """

    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--force', action='store_true', default=False, dest='force',
            help="Force the compiling files even if timestamps are up-to-date."
        )
        parser.add_argument(
            '-p', '--with-pythonpath', action='store_true', default=False, dest='with_pythonpath',
            help="Compile also PYTHONPATH libraries."
        )
        parser.add_argument(
            'path', nargs=argparse.REMAINDER,
            help="Directories with libraries"
        )

    def handle(self, *args, **options):
        quiet = 1 if int(options['verbosity']) < 2 else 0
        dirs = options['path'] or sys.path[:1]
        if options['with_pythonpath']:
            dirs += sys.path[1:]
        for d in dirs:
            d = d or '.'
            if os.path.isdir(d) and os.access(d, os.W_OK):
                for dirname, _, filenames in os.walk(d):
                    for filename in filenames:
                        fullname = os.path.join(dirname, filename)
                        compileall.compile_file(
                            fullname, quiet=quiet, force=options['force'])
            else:
                if int(options['verbosity']) >= 2:
                    self.stdout.write("Skipped %s" % d)
