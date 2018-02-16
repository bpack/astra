
__version__ = '0.0.2'
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from astra import config

db = SQLAlchemy()

def create_app(env_name=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config.by_name[env_name or 'dev'])
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_envvar('ASTRA_CONFIG_FILE', silent=True)

    db.init_app(app)
    import astra.models

    from astra.api import api
    app.register_blueprint(api)

    return app
