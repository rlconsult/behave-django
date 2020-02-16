Usage
=====

Web browser automation
----------------------

You can access the test HTTP server from your preferred web automation
library via ``context.base_url``.  Alternatively, you can use
``context.get_url()``, which is a helper function for absolute paths and
reversing URLs in your Django project.  It takes an absolute path, a view
name, or a model as an argument, similar to `django.shortcuts.redirect`_.

Examples:

.. code-block:: python

    # Using Splinter
    @when(u'I visit "{page}"')
    def visit(context, page):
        context.browser.visit(context.get_url(page))

.. code-block:: python

    # Get context.base_url
    context.get_url()
    # Get context.base_url + '/absolute/url/here'
    context.get_url('/absolute/url/here')
    # Get context.base_url + reverse('view-name')
    context.get_url('view-name')
    # Get context.base_url + reverse('view-name', 'with args', and='kwargs')
    context.get_url('view-name', 'with args', and='kwargs')
    # Get context.base_url + model_instance.get_absolute_url()
    context.get_url(model_instance)

Django’s testing client
-----------------------

Internally, Django's TestCase is used to maintain the test environment. You can
access the TestCase instance via ``context.test``.

.. code-block:: python

    # Using Django's testing client
    @when(u'I visit "{url}"')
    def visit(context, url):
        # save response in context for next step
        context.response = context.test.client.get(url)

Simple testing
--------------

If you only use Django's testing client then behave tests can run
much quicker with the ``--simple`` command line option. In this case
transaction rollback is used for test automation instead of flushing
the database after each scenario, just like in Django's standard
``TestCase``.

No HTTP server is started during the simple testing, so you can't
use web browser automation. Accessing ``context.base_url``
or calling ``context.get_url()`` will raise an exception.

unittest + Django assert library
--------------------------------

Additionally, you can utilize unittest and Django’s assert library.

.. code-block:: python

    @then(u'I should see "{text}"')
    def visit(context, text):
        # compare with response from ``when`` step
        response = context.response
        context.test.assertContains(response, text)

Database transactions per scenario
----------------------------------

Each scenario is run inside a database transaction, just like your
regular TestCases.  So you can do something like:

.. code-block:: python

    @given(u'user "{username}" exists')
    def create_user(context, username):
        # This won't be here for the next scenario
        User.objects.create_user(username=username, password='correcthorsebatterystaple')

And you don’t have to clean the database yourself.

django_ready hook
-----------------

You can add a ``django_ready`` function in your ``environment.py`` file in case
you want to make per-scenario changes inside a transaction.

For example, if you have `factories`_ you want to instantiate on a per-scenario
basis, you can initialize them in ``environment.py`` like this:

.. code-block:: python

    from myapp.main.tests.factories import UserFactory, RandomContentFactory


    def django_ready(context, scenario):
        # This function is run inside the transaction
        UserFactory(username='user1')
        UserFactory(username='user2')
        RandomContentFactory()

Or maybe you want to modify the ``test`` instance:

.. code-block:: python

    from rest_framework.test import APIClient


    def django_ready(context, scenario):
        context.test.client = APIClient()

Fixture loading
---------------

behave-django can load your fixtures for you per feature/scenario. There are
two approaches to this:

* loading the fixtures in ``environment.py``, or
* using a decorator on your step function


Fixtures in environment.py
**************************

In ``environment.py`` we can load our context with the fixtures array.

.. code-block:: python

    def before_all(context):
        context.fixtures = ['user-data.json']

This fixture would then be loaded before every scenario.

If you wanted different fixtures for different scenarios:

.. code-block:: python

    def before_scenario(context, scenario):
        if scenario.name == 'User login with valid credentials':
            context.fixtures = ['user-data.json']
        elif scenario.name == 'Check out cart':
            context.fixtures = ['user-data.json', 'store.json', 'cart.json']
        else:
            # Resetting fixtures, otherwise previously set fixtures carry
            # over to subsequent scenarios.
            context.fixtures = []

You could also have fixtures per Feature too

.. code-block:: python

    def before_feature(context, feature):
        if feature.name == 'Login':
            context.fixtures = ['user-data.json']
            # This works because behave will use the same context for
            # everything below Feature. (Scenarios, Outlines, Backgrounds)
        else:
            # Resetting fixtures, otherwise previously set fixtures carry
            # over to subsequent features.
            context.fixtures = []

Of course, since ``context.fixtures`` is really just a list, you can mutate it
however you want, it will only be processed upon leaving the
``before_scenario()`` function of your ``environment.py`` file. Just keep in
mind that it does not reset between features or scenarios, unless explicitly
done so (as shown in the examples above).

.. note::

    If you provide initial data via Python code `using the ORM`_ you need
    to place these calls in ``before_scenario()`` even if the data is
    meant to be used on the whole feature.  This is because Django's
    ``LiveServerTestCase`` resets the test database after each scenario.


Fixtures using a decorator
**************************

You can define `Django fixtures`_ using a function decorator. The decorator will
load the fixtures in the ``before_scenario``, as documented above. It is merely
a convenient way to keep fixtures close to your steps.

.. code-block::  python

    from behave_django.decorators import fixtures

    @fixtures('users.json')
    @when('someone does something')
    def step_impl(context):
        pass

.. note::

     Fixtures included with the decorator will apply to all other steps that
     they share a scenario with. This is because behave-django needs to provide
     them to the test environment before processing the particular scenario.


Support for multiple databases
******************************

By default Django only loads fixtures into the ``default`` database.

Use ``before_scenario`` to load the fixtures in all of the databases you have
configured, if your tests rely on the fixtures being loaded in all of them.

.. code-block:: python

    def before_scenario(context, scenario):
        context.multi_db = True

You can read more about it in the `Multiple database docs`_.


Command line options
--------------------

You can use regular behave command line options with the behave
management command.

.. code-block:: bash

    $ python manage.py behave --tags @wip

Additional command line options provided by django_behave:

``--use-existing-database``
***************************

Don't create a test database, and use the database of your default runserver
instead. USE AT YOUR OWN RISK! Only use this option for testing against a
*copy* of your production database or other valuable data. Your tests may
destroy your data irrecoverably.

``--keepdb``
************

Starting with Django 1.8, the ``--keepdb`` flag was added to ``manage.py test``
to facilitate faster testing by using the existing database instead of
recreating it each time you run the test. This flag enables
``manage.py behave --keepdb`` to take advantage of that feature.
|keepdb docs|_.

``--simple``
************

Use Django's simple ``TestCase`` which rolls back the database transaction after
each scenario instead of flushing the entire database. Tests run much quicker,
however HTTP server is not started and therefore web browser automation is
not available.

Behave configuration file
-------------------------

You can use behave’s configuration file.  Just create a ``behave.ini``,
``.behaverc``, ``setup.cfg`` or ``tox.ini`` file in your project’s root
directory and behave will pick it up.  You can read more about it in the
`behave docs`_.

For example, if you want to have your features directory somewhere else.
In your .behaverc file, you can put

.. code-block:: ini

    [behave]
    paths=my_project/apps/accounts/features/
          my_project/apps/polls/features/

Behave should now look for your features in those folders.


.. _django.shortcuts.redirect: https://docs.djangoproject.com/en/stable/topics/http/shortcuts/#redirect
.. _factories: https://factoryboy.readthedocs.io/en/latest/
.. _behave docs: https://behave.readthedocs.io/en/latest/behave.html#configuration-files
.. |keepdb docs| replace:: More information about ``--keepdb``
.. _keepdb docs: https://docs.djangoproject.com/en/stable/topics/testing/overview/#the-test-database
.. _using the ORM: https://docs.djangoproject.com/en/stable/topics/testing/tools/#fixture-loading
.. _Django fixtures: https://docs.djangoproject.com/en/stable/howto/initial-data/#providing-data-with-fixtures
.. _Multiple database docs: https://docs.djangoproject.com/en/stable/topics/testing/tools/#multi-database-support
