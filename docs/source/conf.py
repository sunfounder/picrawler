# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import sphinx_rtd_theme
import time

project = 'SunFounder PiCrawler Kit'
copyright = f'{time.localtime().tm_year}, SunFounder'
author = 'www.sunfounder.com'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_rtd_theme',
    "sphinx.ext.intersphinx",
]

# -- sphinx_rtd_theme Theme options -----------------------------------------------------
html_theme_options = {
    'flyout_display': 'attached'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# Link to other projects’ documentation with intersphinx. Use the intersphinx_mapping configuration to indicate the name and link of the projects you want to use


intersphinx_mapping = {
    'ezblock': ('https://docs.sunfounder.com/projects/ezblock3/en/latest/', None),
}



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


html_js_files = [
    'https://ezblock.cc/readDocFile/custom.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/ace.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-python.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/mode-sh.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/monokai.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/xterm.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/FitAddon.js',
    'https://ezblock.cc/readDocFile/readTheDoc/src/js/readTheDocIndex.js',
]
html_css_files = [
    'https://ezblock.cc/readDocFile/custom.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/index.css',
    'https://ezblock.cc/readDocFile/readTheDoc/src/css/xterm.css',
]
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

language = 'en'
locale_dirs = ['locale/'] 

gettext_compact = False

# open link in a new window

rst_epilog = """

.. |link_it_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/it/latest/" target="_blank">Tutorial online in italiano</a>

.. |link_es_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/es/latest/" target="_blank">Tutoriales en línea en español</a>

.. |link_fr_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/fr/latest/" target="_blank">Didacticiels en ligne en français</a>

.. |link_en_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/en/latest/" target="_blank">English Online-tutorials</a>

.. |link_ja_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/ja/latest/" target="_blank">日本語オンライン教材</a>

.. |link_german_tutorials| raw:: html

    <a href="https://docs.sunfounder.com/projects/pi-crawler/de/latest/" target="_blank">Deutsch Online-Kurs</a>
    
.. |link_robot_hat_v4| raw:: html

    <a href="https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/" target="_blank">Robot HAT</a>

.. |link_voice_options| raw:: html

    <a href="https://platform.openai.com/docs/guides/text-to-speech/voice-options" target="_blank">Voice options</a>

.. |link_iso_language_code| raw:: html

    <a href="https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes" target="_blank">ISO-639</a>

.. |link_openai_platform| raw:: html

    <a href="https://platform.openai.com/api-keys" target="_blank">OpenAI Platform</a>

.. |link_microphone| raw:: html

    <a href="https://www.sunfounder.com/products/mini-usb-microphone?_pos=2&_sid=d05c80026&_ss=r" target="_blank">Microphone link</a>

.. |link_sf_facebook| raw:: html

    <a href="https://bit.ly/raphaelkit" target="_blank">ここ</a>

.. |link_robot_hat| raw:: html

    <a href="https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/hardware_introduction.html" target="_blank">SunFounder Robot HAT</a>

.. |link_Pi_Crawler| raw:: html

    <a href="https://www.sunfounder.com/products/picrawler-robot-kit?_pos=1&_sid=2ebeb7ad0&_ss=r" target="_blank">Purchase Link for PiCrawler</a>

.. |link_PiCrawler| raw:: html

    <a href="https://www.sunfounder.com/products/picrawler-robot-kit?_pos=1&_sid=2ebeb7ad0&_ss=r" target="_blank">PiCrawler</a>

"""
