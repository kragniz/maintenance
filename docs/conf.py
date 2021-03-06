"""Sphinx configuration file"""

import sys
import os

# Enable custom extensions
sys.path.append(os.path.abspath('sphinxext'))
extensions = ['status']

# Use the Read The Docs theme when building offline
if not os.environ.get('READTHEDOCS', None):
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add custom CSS
html_static_path = ['_static']


def setup(app):
    app.add_stylesheet('custom.css')

# General configuration
master_doc = 'index'
exclude_patterns = ['_build', '*/examples/*', 'references.rst']

# Project information
project = u'Maintenance'
copyright = u'2014, Sam Clements'
version = release = '0.0.0'
