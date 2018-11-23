import structlog


logger = structlog.getLogger()


def no_output():
    logger.info = lambda *_, **__: None


no_output()
