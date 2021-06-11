from logging.config import dictConfig

"""
We have options in python for stdout (streamhandling) and file logging
File logging has options for a Rotating file based on size or time (daily)
or a watched file, which supports logrotate style rotation
Most of the changes happen in the handlers, lets define a few standards
"""


class LogSetup(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app):
        log_type = app.config["LOG_TYPE"]
        logging_level = app.config["LOG_LEVEL"]
        if log_type != "stream":
            try:
                log_directory = app.config["LOG_DIR"]
                app_log_file_name = app.config["APP_LOG_NAME"]
                access_log_file_name = app.config["WWW_LOG_NAME"]
                info_log_file_name = app.config["INFO_LOG_NAME"]
                warn_log_file_name = app.config["WARN_LOG_NAME"]
                error_log_file_name = app.config["ERROR_LOG_NAME"]
            except KeyError as e:
                exit(code="{} is a required parameter for log_type '{}'".format(e, log_type))

            www_log = "/".join([log_directory, access_log_file_name])
            app_log = "/".join([log_directory, app_log_file_name])
            info_log = "/".join([log_directory, info_log_file_name])
            warn_log = "/".join([log_directory, warn_log_file_name])
            error_log = "/".join([log_directory, error_log_file_name])

        if log_type == "stream":
            logging_policy = "logging.StreamHandler"
        else:
            log_copies = app.config["LOG_COPIES"]
            logging_policy = "logging.handlers.TimedRotatingFileHandler"

        std_format = {
            "formatters": {
                "default": {
                    "format": "[%(asctime)s.%(msecs)03d] %(levelname)s %(name)s:%(funcName)s: %(message)s",
                    "datefmt": "%d/%b/%Y:%H:%M:%S",
                },
                "access": {"format": "%(message)s"},
                "info": {"format": "%(message)s"},
                "error": {"format": "%(message)s"},
            }
        }
        std_logger = {
            "loggers": {

                "": {"level": logging_level,
                     "handlers": ["default"],
                     "propagate": True
                     },
                "app": {
                    "level": logging_level,
                    "handlers": ["info_logs", "warn_logs", "error_logs"],
                    "propagate": False,
                },
                "access": {
                    "level": logging_level,
                    "handlers": ["access_logs"],
                    "propagate": False,
                }
            }
        }
        if log_type == "stream":
            logging_handler = {
                "handlers": {
                    "default": {
                        "level": logging_level,
                        "class": logging_policy,
                        "formatter": "default"
                    },
                    "info_logs": {
                        "level": "INFO",
                        "class": logging_policy,
                        "formatter": "access",
                    },
                    "warn_logs": {
                        "level": "INFO",
                        "class": logging_policy,
                        "formatter": "access"
                    },
                    "error_logs": {
                        "level": "ERROR",
                        "class": logging_policy,
                        "formatter": "access"
                    },
                    "access_logs": {
                        "level": logging_level,
                        "class": logging_policy,
                        "formatter": "access"
                    }

                }
            }
        else:
            logging_handler = {
                "handlers": {
                    "default": {
                        "level": logging_level,
                        "class": logging_policy,
                        "filename": app_log,
                        "backupCount": log_copies,
                        "formatter": "default",
                        "delay": True,
                        "when": "D",
                    },
                    "info_logs": {
                        "level": "INFO",
                        "class": logging_policy,
                        "filename": info_log,
                        "formatter": "access",
                        "delay": True,
                        "when": "D",
                    },
                    "warn_logs": {
                        "level": "INFO",
                        "class": logging_policy,
                        "filename": warn_log,
                        "formatter": "access",
                        "delay": True,
                        "when": "D",
                    },
                    "error_logs": {
                        "level": "ERROR",
                        "class": logging_policy,
                        "filename": error_log,
                        "formatter": "access",
                        "delay": True,
                        "when": "D",
                    },
                    "access_logs": {
                        "level": logging_level,
                        "class": logging_policy,
                        "filename": www_log,
                        "backupCount": log_copies,
                        "formatter": "access",
                        "delay": True,
                        "when": "D",
                    },
                }
            }

        log_config = {
            "version": 1,
            "formatters": std_format["formatters"],
            "loggers": std_logger["loggers"],
            "handlers": logging_handler["handlers"],
        }
        dictConfig(log_config)
