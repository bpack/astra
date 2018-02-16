import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    ASTRA_MESSAGE = 'Astra is running'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'astra.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    ASTRA_MESSAGE = 'Astra is running (in development mode)'

class ProductionConfig(Config):
    pass

by_name = dict(
    dev = DevelopmentConfig,
    prod = ProductionConfig
)


