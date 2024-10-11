# conf.py
# Sphinx configuration file
# https://www.sphinx-doc.org/en/master/usage/configuration.html

### import setup ##################################################################################

import datetime

### project information ###########################################################################

project = "sentier_peakachu"
author = "Brightway Developers"
copyright = datetime.date.today().strftime("%Y") + ' Brightway Developers'

### project configuration #########################################################################

extensions = [
    # core extensions
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    # iPython extensions
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
    # Markdown support
    # 'myst_parser', # do not enable separately if using myst_nb, compare: https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # Jupyter Notebook support
    "myst_nb",
    # mermaid support
    "sphinxcontrib.mermaid",
    # API documentation support
    "autoapi",
    # responsive web component support
    "sphinx_design",
    # custom 404 page
    "notfound.extension",
    # custom favicons
    "sphinx_favicon",
    # copy button on code blocks
    "sphinx_copybutton",
]

napoleon_numpy_docstring = True

exclude_patterns = ['_build']

# The master toctree document.
master_doc = 'index'

### intersphinx configuration ######################################################################

intersphinx_mapping = {
    "bw": ("https://docs.brightway.dev/en/latest/", None),
}    

### theme configuration ############################################################################

html_theme = "pydata_sphinx_theme"
html_title = "sentier_peakachu"
html_show_sphinx = False

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    "logo": {
        "text": "sentier_peakachu",
        "image_light": "https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/source/_static/logo/BW_all_black_transparent_landscape.svg",
        "image_dark": "https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/source/_static/logo/BW_all_white_transparent_landscape.svg",
    },
}

html_logo = 'https://raw.githubusercontent.com/brightway-lca/brightway-documentation/main/source/_static/logo/BW_all_white_transparent_landscape_wide.svg'
html_favicon = 'https://github.com/brightway-lca/brightway-documentation/blob/main/source/_static/logo/BW_favicon_500x500.png'

### extension configuration ########################################################################

## myst_parser configuration ############################################
## https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

## autoapi configuration ################################################
## https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#customisation-options

source_suffix = {".rst": "restructuredtext", ".md": "myst-nb", ".ipynb": "myst-nb"}

autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance',
    'show-module-summary',
]

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_root = 'content/api'
autoapi_keep_files = False

autoapi_dirs = [
    '../sentier_peakachu',
]

autoapi_ignore = [
    '*/data/*',
    '*tests/*',
    '*tests.py',
    '*validation.py',
    '*version.py',
    '*.rst',
    '*.yml',
    '*.md',
    '*.json',
    '*.data'
]