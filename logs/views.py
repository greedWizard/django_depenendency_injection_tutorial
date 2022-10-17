from dependency_injector.wiring import inject, Provide

from django.http import HttpRequest, HttpResponse
from logs.containers import CatsContainer

from logs.services import EventLogService

import logging


@inject
def pet_cat_view(
    request: HttpRequest,
    cats_logs_service: EventLogService = Provide[CatsContainer.cats_logs_service],
) -> HttpResponse:
    cats_logs_service.create_log('Pet cat')
    return HttpResponse(content='ok'.encode())


@inject
def feed_cat_view(
    request: HttpRequest,
    cats_logs_service: EventLogService = Provide[CatsContainer.cats_logs_service],
) -> HttpResponse:
    cats_logs_service.create_log('Feed cat')
    return HttpResponse(content='ok'.encode())
