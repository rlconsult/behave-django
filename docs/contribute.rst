Contributing
============

Want to help out with behave-django?  Cool!  Here's a quick guide to do just
that.

Fork, then clone the repo:

.. code:: bash

    $ git clone git@github.com:your-username/behave-django.git

Install the dev dependencies

.. code:: bash

    $ pip install -r requirements-dev.txt

Make sure the tests pass.  The ``@failing`` tag is used for tests that are
supposed to fail.

.. code:: bash

    $ python manage.py behave --tags=~@failing  # skip failing tests
    $ py.test

Start your topic branch

.. code:: bash

    $ git checkout -b your-topic-branch

Make your changes.  Add tests for your change.  Make the tests pass:

.. code:: bash

    $ python manage.py behave --tags=~@failing
    $ py.test

Finally, make sure your tests pass on all the configurations behave-django
supports. We use tox for this.  The Python versions you test against need to
be available in your PATH.

.. code:: bash

    $ tox

You can choose not to run the tox tests, but make sure your tests pass in the
CI server when you push your PR.

Your tests don't have to be behave tests. ``:-)``

Push to your fork and `submit a pull request`_.

Other things to note:

- Write tests.
- We're using PEP8 as our code style guide (``flake8`` with run over the code
  on the CI server).

Thank you!


.. _submit a pull request: https://github.com/behave/behave-django/compare/
