"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import subprocess
import os
import json

# pylint: disable=invalid-name

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "RF24 library"
copyright = "2021, nRF24 org"
author = "nRF24"

# The full version, including alpha/beta/rc tags
release = "1.4.2"  # the minimum version that supports sphinx builds and RTD hosting
with open("../../library.json", "rb") as lib_json:
    # get updated info from PlatformIO JSON
    release = json.load(lib_json)["version"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "breathe",
    "sphinx_immaterial",
    "sphinx.ext.autosectionlabel",
    "sphinx_immaterial.apidoc.cpp.cppreference",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# code-blocks will use this as their default syntax highlighting
highlight_language="c++"
primary_domain="cpp"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# -- Options for breathe (XML output from doxygen) ---------------------------

breathe_projects = {"RF24": "xml"}
breathe_default_project = "RF24"
breathe_show_define_initializer = True
breathe_show_enumvalue_initializer = True
breathe_domain_by_extension = { "h" : "cpp" }

# debug options
# breathe_debug_trace_directives = True
# breathe_debug_trace_doxygen_ids = True
# breathe_debug_trace_qualification = True

READTHEDOCS = os.environ.get('READTHEDOCS', None) == 'True'

if READTHEDOCS:
    subprocess.call("cd ../..; doxygen", shell=True)

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = "sphinx_rtd_theme"
html_theme = "sphinx_immaterial"
html_theme_options = {
    "features": [
        # "navigation.expand",
        "navigation.tabs",
        # "toc.integrate",
        # "navigation.sections",
        "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "search.highlight",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "lime",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-blue",
            "accent": "green",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
    ],
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/nRF24/RF24/",
    "repo_name": "RF24",
    "repo_type": "github",
    # If False, expand all TOC entries
    "globaltoc_collapse": False,
}

object_description_options = [
    ("cpp:functionParam", dict(include_in_toc=False, generate_synopses=None)),
    ("cpp:function", dict(include_fields_in_toc=False)),
]

sphinx_immaterial_custom_admonitions = [
    {
        "name": "warning",
        "color": (255, 66, 66),
        "icon": "octicons/alert-24",
        "override": True,
    },
    {
        "name": "note",
        "icon": "octicons/pencil-24",
        "override": True,
    },
    {
        "name": "seealso",
        "color": (255, 66, 252),
        "icon": "octicons/eye-24",
        "title": "See Also",
        "override": True,
    },
    {
        "name": "remark",
        "color": (116, 66, 255),
        "icon": "octicons/checklist-16",
    },
]

# Set link name generated in the top bar.
html_title = "RF24 C++ library"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["custom_material.css"]

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "_static/new_favicon.ico"

# project logo
html_logo = "_static/Logo large.png"

# split site index page into 2 pages:
# 1 with only alphabet-like links to partial lists, 1 with full listing
html_split_index = True
