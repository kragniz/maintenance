Rust
^^^^

.. toctree::

Packaging
=========

Follow the `Cargo guide`_. Nice and simple.

Testing
=======

Test annotations
----------------

Code can be annotated to mark it as a test.

Cargo
-----

Run tests with `cargo test`.

Travis-CI configuration
-----------------------

For a project using Cargo_, a `.travis.yml` is very simple:

.. code-block:: yaml

    language: rust

Checklist
=========

Creating a new package
----------------------

Package structure
    `cargo new <project>`

Releasing a package
-------------------

Run tests
    `cargo test`

Update metadata
    Change version number in `Cargo.toml`

Tag release
    |git-tag-version|_ *or* ``git tag -a "v0.1.0" -m "Version 0.1.0"``

Package upload
    `cargo publish`

Documentation
-------------

Build documentation
    `cargo doc`

Build and open documentation
    `cargo doc --open`

.. _Cargo: http://doc.crates.io/index.html
.. _Cargo guide: http://doc.crates.io/guide.html
.. include:: ../references.rst
