# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

project = "Library Management System"
copyright = "2023, Library Management System"
author = "Artem Kirillov"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
sys.path.insert(0, os.path.abspath('../../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'webapp.settings'
django.setup()

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.todo',
    'sphinx.ext.autosummary',
    'sphinx_rtd_theme'
]

build_path = '../_build'
if not os.path.exists(build_path):
    os.makedirs(build_path)

folder_path = '../_templates'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

templates_path = [folder_path]

exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store', 'docs/*',
    '**/migrations/*', '**/tests/*'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# -- Sphinx Themes -------------------------------------------------
# https://sphinx-themes.org/#themes

html_theme = 'sphinx_rtd_theme'
html_context = {
    'current_version': '1.0.0',
}
# html_theme = 'sphinx_book_theme'
static_path = '../_static'
if not os.path.exists(static_path):
    os.makedirs(static_path)

html_static_path = [static_path]
