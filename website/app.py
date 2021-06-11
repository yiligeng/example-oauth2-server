import os
from flask import Flask,request,g
from .models import db
from .oauth2 import config_oauth
from .routes import bp
from .extensions import logs

from datetime import datetime as dt

import time

import logging

from .config.config import config

def create_app(config_name):
    app = Flask(__name__)

    # load default configuration
    app.config.from_object(config[config_name])

    # load environment configuration
    if 'WEBSITE_CONF' in os.environ:
        app.config.from_envvar('WEBSITE_CONF')

    register_extensions(app)

    # load app specified configuration
    if config is not None:
        if isinstance(config, dict):
            app.config.update(config)
        elif config.endswith('.py'):
            app.config.from_pyfile(config)

    @app.before_request
    def before_request():
        g.request_start_time = time.time()
        logger = logging.getLogger("access")
        logger.info(
            "Request  ===> TIME: [%s] | IP: %s | METHOD: %s | PATH: %s | REQUEST_ARGS: %s | REQUEST_JSON: %s | REQUEST_FILES: %s | SCHEME: %s | "
            "REFERRER: %s | USER_AGENT: %s |",
            dt.now().strftime("%Y/%m/%d:%H:%M:%S.%f")[:-3],
            request.remote_addr,
            request.method,
            request.path,
            request.args,
            request.json,
            request.files,
            request.scheme,
            request.referrer,
            request.user_agent,
        )

    setup_app(app)
    return app

def register_extensions(app):
    logs.init_app(app)


def setup_app(app):
    # Create tables if they do not exist already
    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    config_oauth(app)
    app.register_blueprint(bp, url_prefix='')
