Maintenance
===========

.. image:: https://readthedocs.org/projects/maintenance/badge/?version=latest&style=flat
    :target: http://maintenance.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/github/issues/borntyping/maintenance.svg?style=flat
    :target: https://github.com/borntyping/maintenance/issues
    :alt: GitHub issues

.. image:: https://img.shields.io/badge/licence-CC--BY--SA-red.svg?style=flat
    :target: https://github.com/borntyping/maintenance/blob/master/README.rst
    :alt: Creative Commons Attribution-ShareAlike 4.0 International License

|

Documentation on maintaining my open-source projects. Most of this will probably cover Python packaging.

Building
--------

::

    pip install -r requirements.txt     # Install required Python packages
    sphinx-build docs docs/_build       # Build the documentation with Sphinx
    xdg-open docs/_build/index.html     # Open the documentation in your browser

Licence
-------

.. image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
    :alt: Creative Commons Attribution-ShareAlike 4.0 International License
    :target: cc-by-sa_

This work is licensed under the |cc-by-sa|_.

Author
------

Written and maintained by `Sam Clements <https://github.com/borntyping>`_.

.. |cc-by-sa| replace:: Creative Commons Attribution-ShareAlike 4.0 International License
.. _cc-by-sa: http://creativecommons.org/licenses/by-sa/4.0/
