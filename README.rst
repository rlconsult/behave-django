behave-django
=============

|Build Status| |Latest Version|

Behave BDD integration for Django

Features
--------

-  Web Browser Automation ready
-  Database transactions per scenario
-  Use Django's testing client
-  Use unittest + Django assert library
-  Use behave's command line arguments
-  Use behave's configuration file
-  Fixture loading

Installation
------------

Install using pip

.. code:: bash

    $ pip install behave-django

Add ``behave_django`` to your ``INSTALLED_APPS``

.. code:: python

    INSTALLED_APPS += ('behave_django',)

Create the features directory in your project’s root directory. (Next to
``manage.py``)

::

    features/
        steps/
            your_steps.py
        environment.py
        your-feature.feature

Setup your ``environment.py`` file

.. code:: python

    from behave_django import environment

    def before_scenario(context, scenario):
        environment.before_scenario(context, scenario)

    def after_scenario(context, scenario):
        environment.after_scenario(context, scenario)

Run ``python manage.py behave``

::

    $ python manage.py behave
    Creating test database for alias 'default'...
    Feature: Running tests # features/running-tests.feature:1
      In order to prove that behave-django works
      As the Maintainer
      I want to test running behave against this features directory
      Scenario: The Test                       # features/running-tests.feature:6
        Given this step exists                 # features/steps/running_tests.py:4 0.000s
        When I run "python manage.py behave"   # features/steps/running_tests.py:9 0.000s
        Then I should see the behave tests run # features/steps/running_tests.py:14 0.000s

    1 features passed, 0 failed, 0 skipped
    1 scenarios passed, 0 failed, 0 skipped
    3 steps passed, 0 failed, 0 skipped, 0 undefined
    Took.010s
    Destroying test database for alias 'default'...

What's next?
------------

`Read the docs!`_


Support
-------

behave-django is tested on:

Django 1.4.20, 1.5.12, 1.6.11, 1.7.8, 1.8.2

Python 2.6, 2.7, 3.3, 3.4

It should work on everything, basically.

Contributing
------------

Read the `contributing guide`_

Resources
---------

-  `behave-django documentation`_
-  `behave`_

.. _behave-django documentation: https://pythonhosted.org/behave-django/
.. _Read the docs!: https://pythonhosted.org/behave-django/
.. _behave: https://github.com/behave/behave
.. _contributing guide: https://github.com/mixxorz/behave-django/blob/master/CONTRIBUTING.md
.. |Build Status| image:: https://travis-ci.org/mixxorz/behave-django.svg?branch=master
   :target: https://travis-ci.org/mixxorz/behave-django
.. |Latest Version| image:: https://badge.fury.io/py/behave-django.svg
    :target: http://badge.fury.io/py/behave-django
