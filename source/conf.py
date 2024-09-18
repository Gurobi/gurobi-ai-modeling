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
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_tabs.tabs",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxcontrib.images",
    "sphinx_carousel.carousel",
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

images_config = {
    'default_image_width': '40%',
    'show_caption': True,
    'figure_classes': ['align-center'],
    'lightbox': 'lightbox2',  # or 'fancybox' or other supported lightbox libraries
}

html_theme_options = {
    "version_warning": "false",
    "feedback_banner": "true",
    "construction_warning": "false",
}

intersphinx_disabled_domains = ['std']

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path = ['_static']


def setup(app):
    app.add_css_file('custom.css')
