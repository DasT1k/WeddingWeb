import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'that-is-the-secret-key'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

    MAIL_SERVER = 'smtp.sendgrid.net'  # info can be found in dashboard https://app.sendgrid.com/
    MAIL_PORT = 25  # does not work with SSL (port=465)
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = 'secretKey'
    MAIL_FROM = 'sayonaradjeronimo@yandex.ru'
    ADMINS = ['romanbokhovko@gmail.com']


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
    WTF_CSRF_ENABLED = False
