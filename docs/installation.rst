Installation
============

Install using pip

.. code-block:: bash

    $ pip install behave-django

Add ``behave_django`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS += ('behave_django',)

Create the features directory in your project’s root directory. (Next to
``manage.py``)

::

    features/
        steps/
            your_steps.py
        environment.py
        your-feature.feature

Run ``python manage.py behave``::

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

See the `environment.py`_, `running-tests.feature`_ and `steps/running_tests.py`_
files in the ``features`` folder of the project repository for implementation
details of this very example.  See the folder also for `more useful examples`_.

.. note::

   The `behave docs`_ provide additional helpful information on using *behave*
   with Django and various test automation libraries.

.. note::

   Starting with version ``0.2.0``, you no longer need to insert the
   ``environment.before_scenario()`` and ``environment.after_scenario()``
   functions in your ``environment.py`` file. The hooks are now included via
   monkey patching.


.. _environment.py: https://github.com/behave/behave-django/blob/master/features/environment.py
.. _running-tests.feature: https://github.com/behave/behave-django/blob/master/features/running-tests.feature
.. _steps/running_tests.py: https://github.com/behave/behave-django/blob/master/features/steps/running_tests.py
.. _more useful examples: https://github.com/behave/behave-django/tree/master/features
.. _behave docs: http://pythonhosted.org/behave/django.html#automation-libraries
