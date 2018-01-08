import os

from flask import Flask
from . import config

def create_app(env_name=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.by_name[env_name or 'dev'])
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_envvar('ASTRA_CONFIG_FILE', silent=True)

    @app.route('/')
    def index():
        return app.config['ASTRA_MESSAGE']

    return app


