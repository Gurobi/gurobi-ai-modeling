# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Gurobi AI Modeling"
copyright = "2024, Gurobi Optimization"
author = "Gurobi Optimization"

html_title = "AI Modeling - Gurobi Optimization"
html_theme = "gurobi_sphinxtheme"
html_favicon = "https://www.gurobi.com/favicon.ico"
html_static_path = ["_static"]
templates_path = ["_templates"]

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_carousel.carousel",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_last_updated_by_git",
    "sphinx_tabs.tabs",
    "sphinxcontrib.images",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}

images_config = {
    "default_image_width": "40%",
    "show_caption": True,
    "figure_classes": ["align-center"],
    "lightbox": "lightbox2",  # or "fancybox" or other supported lightbox libraries
}

html_theme_options = {
    "version_warning": False,
    "feedback_banner": True,
    "construction_warning": False,
    "sidebar_hide_name": False,
}

intersphinx_disabled_domains = ["std"]

# -- Options for EPUB output
epub_show_urls = "footnote"

graphviz_output_format = "svg"

def setup(app):
    app.add_css_file("custom.css")
    app.add_css_file("gurobi.css")

# Ignore certain links that are known to fail
linkcheck_ignore = [
    r"https://support.gurobi.com/hc/en-us",
    r"https://support.gurobi.com/hc/en-us/community/topics",
    r"https://github.com/Gurobi/gurobi-modelanalyzer\?tab=readme-ov-file#using-the-solution-checker",
]
