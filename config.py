import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '09c24eb0504e4f29b35240d9e3813afa'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'example@mail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or '123456'
    FLASKY_MAIL_SUBJECT_PREFIX = '[ivany]'
    FLASKY_MAIL_SENDER = ''
    FLASKY_ADMIN = os.environ.get('IVANY_ADMIN') or 'admin'
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME=0.5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/blog'
    WEBSITE = 'http://127.0.0.1'
    BASE_FILEPATH = 'app/templates/'

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/blog'
    WTF_CSRF_ENABLED = False
    WEBSITE = 'http://127.0.0.1'
    BASE_FILEPATH = 'app/templates/'

class ProductionConfig(Config):
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/blog'
    WEBSITE = 'http://ivany.me'
    BASE_FILEPATH = ''

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        # import logging
        # from logging.handlers import SMTPHandler
        # credentials = None
        # secure = None
        # if getattr(cls, 'MAIL_USERNAME', None) is not None:
        #     credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
        #     if getattr(cls, 'MAIL_USE_TLS', None):
        #         secure = ()
        # mail_handler = SMTPHandler(
        #     mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
        #     fromaddr=cls.FLASKY_MAIL_SENDER,
        #     toaddrs=[cls.FLASKY_ADMIN],
        #     subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
        #     credentials=credentials,
        #     secure=secure)
        # mail_handler.setLevel(logging.ERROR)
        # app.logger.addHandler(mail_handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}