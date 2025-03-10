# This code is part of Qiskit.
#
# (C) Copyright IBM 2021.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

# pylint: disable=invalid-name
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("."))

"""
Sphinx documentation builder
"""

import qiskit_sphinx_theme

# Set env flag so that we can doc functions that may otherwise not be loaded
# see for example interactive visualizations in qiskit.visualization.
os.environ['QISKIT_DOCS'] = 'TRUE'

# -- Project information -----------------------------------------------------
project = 'Qiskit Cold Atom'
copyright = '2021, Qiskit Cold Atom Development Team'  # pylint: disable=redefined-builtin
author = 'Qiskit Cold Atom Development Team'

# The short X.Y version
version = "0.1"
# The full version, including alpha/beta/rc tags
release = '0.1.1'

rst_prolog = """
.. raw:: html

    <br><br><br>

.. |version| replace:: {0}
""".format(release)

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. raw:: html

        <br><br><br>

    .. note::
        Run interactively in jupyter notebook.
"""

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinx_tabs.tabs',
    'jupyter_sphinx',
    'sphinx_autodoc_typehints',
    'reno.sphinxext',
    'sphinx.ext.doctest',
    'nbsphinx',
    "qiskit_sphinx_theme",
]
templates_path = ['_templates']

nbsphinx_timeout = 360
nbsphinx_execute = os.getenv('QISKIT_DOCS_BUILD_TUTORIALS', 'never')
nbsphinx_widgets_path = ''
exclude_patterns = ['_build', '**.ipynb_checkpoints']
nbsphinx_thumbnails = {}

# -----------------------------------------------------------------------------
# Autosummary
# -----------------------------------------------------------------------------

autosummary_generate = True
autosummary_generate_overwrite = False

# -----------------------------------------------------------------------------
# Autodoc
# -----------------------------------------------------------------------------

autodoc_default_options = {
    'inherited-members': None,
}

autoclass_content = 'both'

# If true, figures, tables and code-blocks are automatically numbered if they
# have a caption.
numfig = True

# A dictionary mapping 'figure', 'table', 'code-block' and 'section' to
# strings that are used for format of figure numbers. As a special character,
# %s will be replaced to figure number.
numfig_format = {
    'table': 'Table %s'
}
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'colorful'

# A boolean that decides whether module names are prepended to all object names
# (for object types where a “module” of some kind is defined), e.g. for
# py:function directives.
add_module_names = False

# A list of prefixes that are ignored for sorting the Python module index
# (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# This can be handy if you document a project that consists of a single
# package. Works only for the HTML builder currently.
modindex_common_prefix = ["qiskit_cold_atom."]

# -- Configuration for extlinks extension ------------------------------------
# Refer to https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html


# -- Options for HTML output -------------------------------------------------

html_theme = "qiskit_sphinx_theme"

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}
