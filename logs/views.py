from django.http import HttpRequest, HttpResponse

from logs.services import EventLogService

import logging


def pet_cat_view(request: HttpRequest) -> HttpResponse:
    logger = logging.getLogger('cats')
    handler = logging.FileHandler('logs/cats.log')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    logging_service = EventLogService(logger)
    logging_service.create_log('A user pet a cat')
    return HttpResponse(content='ok'.encode())


def feed_cat_view(request: HttpRequest) -> HttpResponse:
    logger = logging.getLogger('cats')
    handler = logging.FileHandler('logs/cats.log')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    logging_service = EventLogService(logger)
    logging_service.create_log('A user fed a cat')
    return HttpResponse(content='ok'.encode())
