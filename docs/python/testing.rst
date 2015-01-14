Testing Python projects
=======================

* Test runners: Tox_, `Travis-CI`_
* Testing: pytest_, mock_
* Style checker: flake8_, `flake8-docstrings`_

Use Tox_ to run tests across multiple versions of Python. Tox installs the package into a virtualenv for each environment and runs the test command inside that.

Most projects should use pytest_, a testing runner and framework that is much easier to use that the ``unittest`` module.

A basic ``tox.ini`` file to use pytest should look like this:

.. code-block:: ini

    [tox]
    minversion=1.8.0
    envlist=py{26,27,33,34}

    [testenv]
    commands=py.test -v {posargs} <MODULE>
    deps=pytest

Configuring `Travis-CI`_ to run Tox_ properly is slightly verbose, but means local and remote tests run in an almost identical fashion. The ``.travis.yml`` file should include each tox environment in it's matrix (see the Configuration_ section below for a full example):

.. code-block:: yaml

    language: python
    env:
      - TOXENV=py26
      - TOXENV=py27
      - TOXENV=py33
      - TOXENV=py34
    install:
      - pip install tox
    script:
      - tox

Style checking
--------------

Use flake8_ to run style checks, which collects pyflakes_, pep8_ and mccabe_. The `flake8-docstrings`_ module extends it to include pep257_. As it reads it's configuration from ``tox.ini``, it can be added to Tox very easily.

.. code-block:: ini

    [testenv:style]
    commands=flake8 <MODULE>
    basepython=python2.7
    deps=
        flake8
        flake8_docstrings

    [flake8]
    ignore=D102,D203

This ignores the following messages:

* ``D102: Function docstring missing``
* ``D203: Expected 1 blank line *before* class docstring, found 0``

Configuration
-------------

A full Tox_ configuration file for a standard python package should run tests on each supported version of Python, run style checkers, and include environments to build documentation and release the package (see the `Python Packaging` page). This configuration allows packages to be built and tested without needing to install any dependancies other than Tox_.

.. code-block:: ini

    [tox]
    minversion=1.8.0
    envlist=py{26,27,33,34},style,docs

    [testenv]
    commands=py.test {posargs} <MODULE>
    deps=pytest

    [pytest]
    addopts=-q

    [testenv:style]
    commands=flake8 <MODULE>
    basepython=python2.7
    deps=
        flake8
        flake8_docstrings

    [flake8]
    ignore=D102,D203

    [testenv:docs]
    commands=sphinx-build -qE docs/ docs/_build/
    deps=
        sphinx
        sphinx_rtd_theme

    [testenv:release]
    commands=python setup.py sdist bdist_wheel upload
    skip_sdist=true
    deps=wheel

`Travis-CI`_ should be configured to run all environments (excluding releasing the package), though style and documentation environments should be allowed to fail. Including ``sudo: true`` will use `Travis-CI's container based build system <http://docs.travis-ci.com/user/workers/container-based-infrastructure/>`_.

.. code-block:: YAML

    language: python
    env:
      - TOXENV=py26
      - TOXENV=py27
      - TOXENV=py33
      - TOXENV=py34
      - TOXENV=style
      - TOXENV=docs
    install:
      - pip install tox
    script:
      - tox
    matrix:
      allow_failures:
        - env: TOXENV=style
        - env: TOXENV=docs
    sudo: true


.. _Tox: http://tox.readthedocs.org/
.. _Travis-CI: http://travis-ci.org/
.. _pytest: http://pytest.org/latest/contents.html
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _flake8: http://flake8.readthedocs.org/
.. _`flake8-docstrings`: https://bitbucket.org/icordasc/flake8-docstrings
.. _pyflakes: https://github.com/pyflakes/pyflakes/
.. _pep8: http://pep8.readthedocs.org/en/latest/
.. _mccabe: http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html
.. _pep257: https://github.com/GreenSteam/pep257
