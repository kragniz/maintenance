Python
^^^^^^

.. toctree::
    :hidden:

    checklist

Packaging
---------

The `Python Packaging User Guide <https://packaging.python.org/en/latest/>`_ has excellent guidance on packaging Python projects - in particular, use the information on `packaging and distributing projects <https://packaging.python.org/en/latest/distributing.html>`_, and the `suggested tools <https://packaging.python.org/en/latest/current.html>`_.

A new python package can be registered to PyPI with:

.. code:: bash

    python setup.py register

Python packages can generally be released with:

.. code:: bash

    python setup.py sdist bdist_wheel upload

Packages that run on Python 2 and 3 should ensure they have a `setup.cfg` file that configures `bdist_wheel` to mark the wheel as 'universal' (otherwise, the wheel will declare that it is only for the version of Python it was built on).

.. code:: ini

    [bdist_wheel]
    universal=1

In the unusual case that a package supplies metadata depending on which Python version it is running on (`example <https://github.com/borntyping/python-riemann-client/blob/master/setup.py>`_), you'll need to run `bdist_wheel` for each of those Python versions. While source distributions run `setup.py` when *installing* a package, built distributions run `setup.py` when creating the package).

.. code:: bash

    python setup.py sdist
    python2 setup.py bdist_wheel
    python3 setup.py bdist_wheel
    twine upload dist/*

Testing
-------

.. note:: `travis-ci`, `tox`_, `pytest`_
