from cyanotype.utils import jinjamarkdown_renderer

""" Configuration Defaults """
DEBUG = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'src'
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_HTML_RENDERER = jinjamarkdown_renderer
#FLATPAGES_MARKDOWN_EXTENSIONS = ['fenced_code']
FREEZER_DESTINATION = 'build'
