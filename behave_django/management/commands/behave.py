from __future__ import absolute_import
import sys

from behave.configuration import options as behave_options
from behave.__main__ import main as behave_main
from django.core.management.base import BaseCommand

from behave_django.environment import monkey_patch_behave
from behave_django.runner import (BehaviorDrivenTestRunner,
                                  ExistingDatabaseTestRunner)


def add_command_arguments(parser):
    """
    Additional command line arguments for the behave management command
    """
    parser.add_argument(
        '--use-existing-database',
        action='store_true',
        default=False,
        help="Don't create a test database. USE AT YOUR OWN RISK!",
    )
    parser.add_argument(
        '-k', '--keepdb',
        action='store_true',
        default=False,
        help="Preserves the test DB between runs.",
    )


def add_behave_arguments(parser):  # noqa
    """
    Additional command line arguments extracted directly from behave
    """

    # Option strings that conflict with Django
    conflicts = [
        '--no-color',
        '--version',
        '-c',
        '-k',
        '-v'
    ]

    parser.add_argument(
        'paths',
        action='store',
        nargs='*',
        help="Feature directory, file or file location (FILE:LINE)."
    )

    for fixed, keywords in behave_options:
        keywords = keywords.copy()

        # Configfile only entries are ignored
        if not fixed:
            continue

        # Build option strings, not including conflicting option strings
        option_strings = []
        for option in fixed:
            if option in conflicts:
                continue

            option_strings.append(option)

        # No use in adding an option if it doesn't have an option string
        if len(option_strings) == 0:
            continue

        # type isn't a valid keyword for make_option
        if hasattr(keywords.get('type'), '__call__'):
            del keywords['type']

        # config_help isn't a valid keyword for make_option
        if 'config_help' in keywords:
            keywords['help'] = keywords['config_help']
            del keywords['config_help']

        parser.add_argument(*option_strings, **keywords)


class Command(BaseCommand):
    help = 'Runs behave tests'

    def add_arguments(self, parser):
        """
        Add behave's and our command line arguments to the command
        """
        usage = "%(prog)s [options] [ [DIR|FILE|FILE:LINE] ]+"
        description = """\
        Run a number of feature tests with behave."""
        parser.usage = usage
        parser.description = description

        add_command_arguments(parser)
        add_behave_arguments(parser)

    def handle(self, *args, **options):

        # Configure django environment
        if options['dry_run'] or options['use_existing_database']:
            django_test_runner = ExistingDatabaseTestRunner()
        else:
            django_test_runner = BehaviorDrivenTestRunner()

        django_test_runner.setup_test_environment()

        if options['keepdb']:
            django_test_runner.keepdb = True

        old_config = django_test_runner.setup_databases()

        # Run Behave tests
        monkey_patch_behave(django_test_runner)
        behave_args = self.get_behave_args()
        exit_status = behave_main(args=behave_args)

        # Teardown django environment
        django_test_runner.teardown_databases(old_config)
        django_test_runner.teardown_test_environment()

        if exit_status != 0:
            sys.exit(exit_status)

    def get_behave_args(self, argv=sys.argv):
        """
        Get a list of those command line arguments specified with the
        management command that are meant as arguments for running behave.
        """
        parser = BehaveArgsHelper().create_parser('manage.py', 'behave')
        args, unknown = parser.parse_known_args(argv[2:])
        return unknown


class BehaveArgsHelper(Command):

    def add_arguments(self, parser):
        """
        Override setup of command line arguments to make behave commands not
        be recognized. The unrecognized args will then be for behave! :)
        """
        add_command_arguments(parser)
