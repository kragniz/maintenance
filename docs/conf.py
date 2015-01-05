"""Sphinx configuration file"""

import sys
import os

# Enable custom extensions
sys.path.append(os.path.abspath('sphinxext'))
extensions = ['packages']

# Use the Read The Docs theme when building offline
if not os.environ.get('READTHEDOCS', None):
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# General configuration
master_doc = 'index'
exclude_patterns = ['_build']

# Project information
project = u'Maintenance'
copyright = u'2014, Sam Clements'
version = release = '0.0.0'
