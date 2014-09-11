from optparse import make_option
import os
import re
import sys

from django.core.management.base import BaseCommand


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
        for d in dirs:
            if os.path.isdir(d) and os.access(d, os.W_OK):
                for dirname, dirnames, filenames in os.walk(d):  # @UnusedVariable
                    for filename in filenames:
                        fullname = os.path.join(dirname, filename)
                        if re.search(self.pattern, fullname):
                            if not options['force']:
                                confirm_action = raw_input("Do you want to delete '%s'? [y/N]  " % fullname)
                                if confirm_action != 'y':
                                    continue
                            os.remove(fullname)
                            if int(options['verbosity']) >= 2:
                                print 'Removed', fullname
            else:
                if int(options['verbosity']) >= 2:
                    print 'Skipped', d
