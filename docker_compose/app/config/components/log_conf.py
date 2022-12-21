log_conf = {
    "version": 1,
    "formatters": {
        "complex": {
            "format": "%(asctime)s.%(msecs)03d\t%(name)s\t%(levelname)s\t%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
    },
    "handlers": {
        "complex_log": {
            "level": "INFO",
            "filename": "django_logger.log",
            "class": "logging.FileHandler",
            "formatter": "complex",
        },
    },
    "loggers": {
        "": {
            "level": "INFO",
            "handlers": ["complex_log"],
        },
    },
}
