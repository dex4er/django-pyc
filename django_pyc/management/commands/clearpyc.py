from optparse import make_option
from django.core.management.base import BaseCommand

import os
import re
import sys


class Command(BaseCommand):
    help = \
    """
    Clears .pyc files from the project.
    """

    pattern = r'^.+\.pyc$'

    option_list = BaseCommand.option_list + (
        make_option('-f', '--force', action="store_true", default=False, dest='force', help='Force the removing files without user interaction.'),
        make_option('-p', '--with-pythonpath', action="store_true", default=False, dest='with_pythonpath', help='Compile also PYTHONPATH libraries.'),
    )

    def handle(self, **options):
        dirs = sys.path if options['with_pythonpath'] else sys.path[:1]
        for dir in dirs:
            if os.path.isdir(dir) and os.access(dir, os.W_OK):
                for dirname, dirnames, filenames in os.walk(dir):  # @UnusedVariable
                    for filename in filenames:
                        full_path = os.path.join(dirname, filename)
                        if re.search(self.pattern, full_path):
                            if not options['force']:
                                confirm_action = raw_input("Do you want to delete '%s'? [y/N]  " % full_path)
                                if confirm_action != 'y':
                                    continue
                            os.remove(full_path)
                            if int(options['verbosity']) >= 2:
                                self.stdout.write("Removed '%s'." % full_path)
            else:
                if int(options['verbosity']) >= 2:
                    self.stdout.write("Skipped '%s'." % dir)
