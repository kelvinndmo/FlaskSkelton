import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']




class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_options = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing':TestingConfig,


}
