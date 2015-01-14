Packaging Python modules
========================

The `Python Packaging User Guide <https://packaging.python.org/en/latest/>`_ has excellent guidance on packaging Python projects - in particular, use the information on `packaging and distributing projects <https://packaging.python.org/en/latest/distributing.html>`_, and the `suggested tools <https://packaging.python.org/en/latest/current.html>`_.

A new python package can be registered to PyPI with:

.. code-block:: bash

    python setup.py register

Python packages can generally be released with:

.. code-block:: bash

    python setup.py sdist bdist_wheel upload

Packages that run on Python 2 and 3 should ensure they have a `setup.cfg` file that configures `bdist_wheel` to mark the wheel as 'universal' (otherwise, the wheel will declare that it is only for the version of Python it was built on).

.. code-block:: ini

    [bdist_wheel]
    universal=1

In the unusual case that a package supplies metadata depending on which Python version it is running on (`example <https://github.com/borntyping/python-riemann-client/blob/master/setup.py>`_), you'll need to run `bdist_wheel` for each of those Python versions. While source distributions run `setup.py` when *installing* a package, built distributions run `setup.py` when creating the package).

.. code-block:: bash

    python setup.py sdist
    python2 setup.py bdist_wheel
    python3 setup.py bdist_wheel
    twine upload dist/*

Tox can be used to automate package releases, by including a test environment that runs the release commands:

.. code-block:: ini

    [testenv:release]
    commands=python setup.py sdist bdist_wheel upload
    skip_sdist=true
    deps=wheel

Readme
------

.. note:: Check that the README is valid with ``rst-lint README.rst``

It's often useful for the README file to include various badges describing the project's status. This block include's the version and licence from PyPi_, the build status from `Travis-CI`_, a link to the project's documentation on `Read The Docs`_, and the number of open GitHub_ issues.

.. code-block:: rst

    .. image:: http://img.shields.io/pypi/v/NAME.svg?style=flat-square
        :target: https://pypi.python.org/pypi/NAME
        :alt: NAME on PyPI

    .. image:: http://img.shields.io/pypi/l/NAME.svg?style=flat-square
        :target: https://pypi.python.org/pypi/NAME
        :alt: NAME on PyPI

    .. image:: https://readthedocs.org/projects/NAME/badge/?version=latest&style=flat-square
        :target: http://NAME.readthedocs.org/en/latest/
        :alt: Documentation for NAME on Read The Docs

    .. image:: http://img.shields.io/travis/borntyping/NAME/master.svg?style=flat-square
        :target: https://travis-ci.org/borntyping/NAME
        :alt: Travis-CI build status for NAME

    .. image:: https://img.shields.io/github/issues/borntyping/NAME.svg?style=flat-square
        :target: https://github.com/borntyping/NAME/issues
        :alt: GitHub issues for NAME

A list of links to the package source, documenation and packages are useful, especially when the README is shown in multiple places:

.. code-block:: rst

    * `Source on GitHub <https://github.com/borntyping/NAME>`_
    * `Documentation on Read the Docs <http://NAME.readthedocs.org/en/latest/>`_
    * `Packages on PyPI <https://pypi.python.org/pypi/NAME>`_
    * `Builds on Travis CI <https://travis-ci.org/borntyping/NAME>`_

.. _PyPI: https://pypi.python.org/pypi/
.. _`Travis-CI`: https://travis-ci.org/
.. _`Read The Docs`: https://readthedocs.org/
.. _GitHub:  https://github.com/

