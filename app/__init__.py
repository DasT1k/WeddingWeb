from flask import Flask
import logging, os
from logging.handlers import RotatingFileHandler, SMTPHandler


def create_app():  # application factory
    app = Flask(__name__)
    config_type = os.environ.get('CONFIG_TYPE') or 'config.Config'  # needed to switch to test config
    app.config.from_object(config_type)

    from app import routes
    app.register_blueprint(routes.bp)  # needed to find the routes

    from app.models import db
    db.init_app(app)

    with app.app_context():  # create DB tables if not exist
        db.create_all()

    initialize_loggers(app, config_type)

    return app


def initialize_loggers(app, config_type):
    if not os.path.exists('logs'):  # create directory for logs if not exists
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/website.log', maxBytes=102400,
                                       backupCount=10)  # keep 10 last log files size of 100kb
    log_format = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')  # custom formatting for the log messages
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Website startup')  # writes to the logs each time server starts

    if config_type == 'config.Config':  # mail alerts to be sent only for prod config
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr=app.config['MAIL_FROM'],
            toaddrs=app.config['ADMINS'],
            subject='Wedding website Error',
            credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']),
            secure=()
        )
        mail_handler.setFormatter(log_format)
        mail_handler.setLevel(logging.ERROR)  # send email when error occur
        app.logger.addHandler(mail_handler)
