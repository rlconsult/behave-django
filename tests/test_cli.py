from imp import reload
import os
from subprocess import PIPE, Popen

from .util import DjangoSetupMixin


def run_silently(command):
    """Run a shell command and return both exit_status and console output."""
    command_args = command.split()
    process = Popen(
        command_args, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    stdout, stderr = process.communicate()
    output = (stdout.decode('UTF-8') + os.linesep +
              stderr.decode('UTF-8')).strip()
    return process.returncode, output


class TestCommandLine(DjangoSetupMixin):

    def test_additional_management_command_options(self):
        exit_status, output = run_silently('python manage.py behave --help')
        assert exit_status == 0
        assert (
            os.linesep + '  --use-existing-database' + os.linesep) in output

    def test_should_accept_behave_arguments(self):
        from behave_django.management.commands.behave import Command
        command = Command()
        args = command.get_behave_args(
            argv=['manage.py', 'behave',
                  '--format', 'progress',
                  '--settings', 'test_project.settings',
                  'features/running-tests.feature'])

        assert '--format' in args
        assert 'progress' in args

    def test_should_not_include_non_behave_arguments(self):
        from behave_django.management.commands.behave import Command
        command = Command()
        args = command.get_behave_args(
            argv=['manage.py', 'behave',
                  '--format', 'progress',
                  '--settings', 'test_project.settings',
                  'features/running-tests.feature'])

        assert '--settings' not in args
        assert 'test_project.settings' not in args

    def test_should_return_positional_args(self):
        from behave_django.management.commands.behave import Command
        command = Command()
        args = command.get_behave_args(
            argv=['manage.py', 'behave',
                  '--format', 'progress',
                  '--settings', 'test_project.settings',
                  'features/running-tests.feature'])

        assert 'features/running-tests.feature' in args

    def test_no_arguments_should_not_cause_issues(self):
        from behave_django.management.commands.behave import Command
        command = Command()
        args = command.get_behave_args(
            argv=['manage.py', 'behave'])

        assert args == []

    def test_command_import_dont_patch_behave_options(self):
        # We reload the tested imports because they
        # could have been imported by previous tests.
        import behave.configuration
        reload(behave.configuration)
        behave_options_backup = [
            (first, second.copy())
            for (first, second) in behave.configuration.options
        ]

        import behave_django.management.commands.behave
        reload(behave_django.management.commands.behave)

        assert behave.configuration.options == behave_options_backup
