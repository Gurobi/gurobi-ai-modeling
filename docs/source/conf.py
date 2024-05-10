# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Gurobi AI Modeling"
copyright = "2024, Gurobi Optimization"
author = "Gurobi Optimization"

html_title = "AI Modeling - Gurobi Optimization"
html_theme = "gurobi_sphinxtheme"
html_favicon = "https://www.gurobi.com/favicon.ico"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- Options for EPUB output
epub_show_urls = 'footnote'
