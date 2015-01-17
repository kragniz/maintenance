Testing Python projects
=======================

* Test runners: Tox_, `Travis-CI`_
* Testing: pytest_, mock_
* Style checker: flake8_, `flake8-docstrings`_

Use Tox_ to run tests across multiple versions of Python. Tox installs the package into a virtualenv for each environment and runs the test command inside that.

Most projects should use pytest_, a testing runner and framework that is much easier to use that the ``unittest`` module.

A basic ``tox.ini`` file to use pytest should look like this:

.. literalinclude:: examples/tox.ini
    :language: ini
    :emphasize-lines: 5-7
    :end-before: [testenv:style]

Configuring `Travis-CI`_ to run Tox_ properly is slightly verbose, but means local and remote tests run in an almost identical fashion. The ``.travis.yml`` file should include each tox environment in it's matrix (see the Configuration_ section below for a full example):

.. literalinclude:: examples/travis.yml
    :language: yaml
    :end-before: matrix:

Style and lint checking
-----------------------

Use flake8_ to run style and lint checks, which collects pyflakes_, pep8_ and mccabe_. The `flake8-docstrings`_ module extends it to include pep257_. As it reads it's configuration from ``tox.ini``, it can be added to Tox very easily.

.. literalinclude:: examples/tox.ini
    :language: ini
    :lines: 12-20

This ignores the following messages:

.. code::

    D102: Function docstring missing
    D203: Expected 1 blank line *before* class docstring, found 0

Configuration
-------------

A full Tox_ configuration file for a standard python package should run tests on each supported version of Python, run style checkers, and include environments to build documentation and release the package (see the `Python Packaging <packaging>`_ page). This configuration allows packages to be built and tested without needing to install any dependancies other than Tox_.

.. literalinclude:: examples/tox.ini
    :language: ini

`Travis-CI`_ should be configured to run all environments (excluding releasing the package), though style and documentation environments should be allowed to fail. Including ``sudo: true`` will use `Travis-CI's container based build system <http://docs.travis-ci.com/user/workers/container-based-infrastructure/>`_.

.. literalinclude:: examples/travis.yml
    :language: yaml

.. _Tox: https://tox.readthedocs.org/
.. _Travis-CI: https://travis-ci.org/
.. _pytest: http://pytest.org/latest/contents.html
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _flake8: https://flake8.readthedocs.org/
.. _`flake8-docstrings`: https://bitbucket.org/icordasc/flake8-docstrings
.. _pyflakes: https://github.com/pyflakes/pyflakes/
.. _pep8: https://pep8.readthedocs.org/en/latest/
.. _mccabe: http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html
.. _pep257: https://github.com/GreenSteam/pep257
