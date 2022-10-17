
import logging

from dependency_injector.providers import Factory

from dependency_injector.containers import DeclarativeContainer

from .services import EventLogService


def get_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    handler = logging.FileHandler(f'logs/{logger_name}.log')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


class CatsContainer(DeclarativeContainer):
    cats_logger = Factory(get_logger, logger_name='cats')
    cats_logs_service = Factory(EventLogService, logger=cats_logger)

