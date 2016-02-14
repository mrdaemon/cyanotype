from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

app.config.from_object('cyanotype.config_defaults')
app.config.from_envvar('CYANOTYPE_CONFIGURATION')

flatpages = FlatPages(app)
freezer = Freezer(app)

import cyanotype.core
