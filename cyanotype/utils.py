from flask import Flask, render_template_string
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown

def jinjamarkdown_renderer(text):
    """
    A custom renderer that runs pygmented markdown through jinja2 first.
    I actually wish to be able to include some markup in my flat files.

    """

    jinja_body = render_template_string(text)
    return pygmented_markdown(jinja_body)
