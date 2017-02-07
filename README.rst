behave-django |latest-version|
==============================

|build-status| |health| |python-support| |downloads| |license| |gitter|

Behave BDD integration for Django

.. features-marker

Features
--------

-  Web Browser Automation ready
-  Database transactions per scenario
-  Use Django's testing client
-  Use unittest + Django assert library
-  Use behave's command line arguments
-  Use behave's configuration file
-  Fixture loading

.. support-marker

Version Support
---------------

behave-django supports all newer Django versions and their supported Python
versions.  Specifically, our tests cover Django 1.8 and above on Python 2.7,
3.3 and above.

The version of `behave`_ is independent from our integration.

**Older versions:** Django versions 1.4 through 1.9 on Python 2.6 through 3.5
are supported until `version 0.3.0`_ of ``behave-django``.  Please install
that release for Django 1.7.x and below.  There is no technical disadvantage.

.. docs-marker

Documentation
-------------

-  Documentation is available from `behave-django.readthedocs.io`_
-  Read more about ``behave`` at `behave.readthedocs.io`_

.. contribute-marker

How to Contribute
-----------------

Please, read the `contributing guide`_ in the docs.

.. references-marker


.. _version 0.3.0: https://pypi.python.org/pypi/behave-django/0.3.0
.. _behave: https://pypi.python.org/pypi/behave
.. _behave-django.readthedocs.io: https://behave-django.readthedocs.io/en/latest/
.. _behave.readthedocs.io: https://behave.readthedocs.io/en/latest/django.html
.. _contributing guide: https://behave-django.readthedocs.io/en/latest/contribute.html
.. |latest-version| image:: https://img.shields.io/pypi/v/behave-django.svg
    :target: https://pypi.python.org/pypi/behave-django/
    :alt: Latest version
.. |build-status| image:: https://img.shields.io/travis/behave/behave-django/master.svg
    :target: https://travis-ci.org/behave/behave-django
    :alt: Build status
.. |health| image:: https://landscape.io/github/behave/behave-django/master/landscape.svg?style=flat
    :target: https://landscape.io/github/behave/behave-django/master
    :alt: Code health
.. |python-support| image:: https://img.shields.io/pypi/pyversions/behave-django.svg
   :target: https://pypi.python.org/pypi/behave-django
   :alt: Python versions
.. |downloads| image:: https://img.shields.io/pypi/dm/behave-django.svg
    :target: https://pypi.python.org/pypi/behave-django/
    :alt: Monthly downloads
.. |license| image:: https://img.shields.io/pypi/l/behave-django.svg
    :target: https://github.com/behave/behave-django/blob/master/LICENSE
    :alt: Software license
.. |gitter| image:: https://badges.gitter.im/behave/behave-django.svg
   :alt: Gitter chat room
   :target: https://gitter.im/behave/behave-django
