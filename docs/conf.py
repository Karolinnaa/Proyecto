import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = '.rst'
master_doc = 'index'
project = 'Nombre de tu proyecto'
version = '1.0'
release = '1.0.0'
language = 'es'
html_static_path = ['_static']
html_theme = 'alabaster'
htmlhelp_basename = 'Django_proyecto'

# Extension configuration
autodoc_member_order = 'bysource'