Maintenance
===========

.. image:: https://readthedocs.org/projects/maintenance/badge/?version=latest&style=flat
    :target: http://maintenance.readthedocs.org/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/github/issues/borntyping/maintenance.svg?style=flat
    :target: https://github.com/borntyping/maintenance/issues
    :alt: GitHub issues

.. image:: https://img.shields.io/badge/licence-CC--BY--SA-green.svg?style=flat
    :target: https://github.com/borntyping/maintenance/blob/master/README.rst
    :alt: Creative Commons Attribution-ShareAlike 4.0 International License

|

Documentation on maintaining my open-source projects. Most of this will probably cover Python packaging.

Setup
-----

Install Sphinx_::

    pip install --user -r requirements.txt

Building
--------

Run Sphinx_ on the documentation::

    sphinx-build docs docs/_build

Open the index using your browser::

    xdg-open docs/_build/index.html

Rebuild the documenation when files are changed (requires `watch-fs`_)::

    watch-fs -d docs 'sphinx-build -E docs docs/_build'

.. _`watch-fs`: https://github.com/borntyping/watch-fs

Style
-----

Use code blocks marked with the language where possible:

.. code:: rst

    .. code:: bash

        function error() { exit 1; }

Licence
-------

.. image:: https://i.creativecommons.org/l/by-sa/4.0/88x31.png
    :alt: Creative Commons Attribution-ShareAlike 4.0 International License
    :target: cc-by-sa_

This work is licensed under the |cc-by-sa|_.

Author
------

Written and maintained by `Sam Clements <https://github.com/borntyping>`_.

.. _Sphinx: http://sphinx-doc.org/
.. |cc-by-sa| replace:: Creative Commons Attribution-ShareAlike 4.0 International License
.. _cc-by-sa: http://creativecommons.org/licenses/by-sa/4.0/
