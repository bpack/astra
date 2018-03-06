import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    ASTRA_MESSAGE = 'Astra is running'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'astra.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfiguration(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'astra-test.db')


class DevelopmentConfig(Config):
    DEBUG = True
    ASTRA_MESSAGE = 'Astra is running (in development mode)'

class ProductionConfig(Config):
    pass

by_name = dict(
    dev = DevelopmentConfig,
    prod = ProductionConfig,
    test = TestConfiguration
)


