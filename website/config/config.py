import os
from datetime import timedelta
import datetime
import logging

basedir = os.path.abspath(os.path.dirname(__file__))


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)



class BaseConfig:  # 基本配置
    SECRET_KEY = 'secrect'
    PERMANENT_SESSION_LIFETIME = timedelta(days=14)

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=1)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    JWT_TOKEN_LOCATION = ['cookies']

    # Set True When Production Env
    JWT_COOKIE_SECURE = False

    OAUTH2_REFRESH_TOKEN_GENERATOR=True

    SQLALCHEMY_TRACK_MODIFICATIONS=True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://postgres:gyl7504928@localhost:5440/oauth2_test'

    DEBUG = True
    TESTING = True
    POSGRE_PARAMS = {
        'database': 'info_vin',
        'user': 'postgres',
        'password': 'gyl7504928',
        'host': 'localhost',
        'port': 5440
    }
    # Logging Setup
    LOG_TYPE = "stream"
    LOG_LEVEL = "INFO"

    # File Logging Setup
    LOG_DIR = "/Users/gengyili/projects/deltamotion_transmission/logs"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"
    INFO_LOG_NAME = "info.log"
    WARN_LOG_NAME = "warn.log"
    ERROR_LOG_NAME = "error.log"
    LOG_MAX_BYTES = 100_000_000
    LOG_COPIES = 30
    logging.getLogger('werkzeug').disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'

    # ?ssl_key=config/client-key.pem&ssl_cert=config/client-cert.pem"


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    POSGRE_PARAMS = {
        'database': 'info_vin',
        'user': 'postgres',
        'password': 'gyl7504928',
        'host': 'localhost',
        'port': 5440
    }
    # Logging Setup
    LOG_TYPE = "stream"
    LOG_LEVEL = "INFO"

    # File Logging Setup
    LOG_DIR = "/data/logs"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"
    INFO_LOG_NAME = "info.log"
    WARN_LOG_NAME = "warn.log"
    ERROR_LOG_NAME = "error.log"
    LOG_MAX_BYTES = 100_000_000
    LOG_COPIES = 30
    logging.getLogger('werkzeug').disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'


class Product(BaseConfig):
    DEBUG = True
    POSGRE_PARAMS = {
        'database': 'info_vin',
        'user': 'postgres',
        'password': 'gyl7504928',
        'host': 'localhost',
        'port': 5440
    }
    # Logging Setup
    LOG_TYPE = "file"
    LOG_LEVEL = "INFO"

    # File Logging Setup
    LOG_DIR = "/data/logs"
    APP_LOG_NAME = "app.log"
    WWW_LOG_NAME = "www.log"
    INFO_LOG_NAME = "info.log"
    WARN_LOG_NAME = "warn.log"
    ERROR_LOG_NAME = "error.log"
    LOG_MAX_BYTES = 100_000_000
    LOG_COPIES = 30
    logging.getLogger('werkzeug').disabled = True
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
    'product': Product,
}
