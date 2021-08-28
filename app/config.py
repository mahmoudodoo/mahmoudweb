import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI ='postgresql://wottrysfll:5EQ508PPYYFW8033$@mahmoudweb-server.postgres.database.azure.com/postgres'
    #SQLALCHEMY_DATABASE_URI ='postgresql://modoo:admin@localhost/mahmoudweb'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    POSTS_PER_PAGE = 25
    STATIC_PATH = os.path.join(basedir,'static')
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
