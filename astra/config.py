import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    ASTRA_MESSAGE = 'Astra is running'

class DevelopmentConfig(Config):
    DEBUG = True
    ASTRA_MESSAGE = 'Astra is running (in development mode)'

class ProductionConfig(Config):
    pass

by_name = dict(
    dev = DevelopmentConfig,
    prod = ProductionConfig
)


