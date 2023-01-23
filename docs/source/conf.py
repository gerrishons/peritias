# Configuration file for the Sphinx documentation builder.

# -- Project information
import os

project = 'Peritia'
copyright = '2022, Scalabli'
author = 'Gerrishon Sirere'

release = '2022.1'
version = '2022.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'notfound.extension'
    'secretum_sphinx_theme'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

html_theme = 'rtd_sphinx_theme'
html_logo = "images/peritia.png"

html_static_path = ["_static"]

html_css_files = ['css/quo_theme.css']
html_theme_options = {'collapse_navigation': False, 'logo_only': True}
# -- Options for EPUB output
epub_show_urls = 'footnote'