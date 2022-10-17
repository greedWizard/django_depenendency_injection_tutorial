from django.db import models

from django.utils import timezone


class EventTypeChoices(models.TextChoices):
    VISIT = ('visit', 'a user visit')
    POST = ('post', 'a user post some data')


class EventLog(models.Model):
    datetime = models.DateTimeField(verbose_name='Время события', default=timezone.now)
    event_type = models.CharField(verbose_name='Тип события', default=EventTypeChoices.VISIT, max_length=150)
