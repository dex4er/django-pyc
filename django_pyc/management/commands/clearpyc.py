import argparse
import os
import re
import sys

from django.core.management import base


class Command(base.BaseCommand):
    help = \
        """
        Clears .pyc files from the project.
        """

    pattern = r'^.+\.pyc$'

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', dest='noinput', action='store_true', default=False,
            help="Do NOT prompt the user for input of any kind."
        )
        parser.add_argument(
            '-f', '--force', dest='force', action='store_true', default=False,
            help="Force the removing files without user interaction."
        )
        parser.add_argument(
            '-p', '--with-pythonpath', dest='with_pythonpath', action='store_true', default=False,
            help="Remove also PYTHONPATH libraries."
        )
        parser.add_argument(
            'path', nargs=argparse.REMAINDER,
            help="Directories with libraries"
        )

    def handle(self, *args, **options):
        dirs = options['path'] or sys.path[:1]
        if options['with_pythonpath']:
            dirs += sys.path[1:]
        for d in dirs:
            d = d or '.'
            if os.path.isdir(d) and os.access(d, os.W_OK):
                for dirname, _, filenames in os.walk(d):
                    for filename in filenames:
                        fullname = os.path.join(dirname, filename)
                        if re.search(self.pattern, fullname):
                            if not options['force'] and not options['noinput']:
                                confirm_action = input(
                                    "Do you want to delete '%s'? [y/N]  " % fullname)
                                if confirm_action != 'y':
                                    continue
                            os.remove(fullname)
                            if int(options['verbosity']) >= 2:
                                self.stdout.write("Removed %s" % fullname)
            else:
                if int(options['verbosity']) >= 2:
                    self.stdout.write("Skipped %s" % d)
