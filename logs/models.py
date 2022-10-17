from django.db import models
from django.utils import timezone


class EventLog(models.Model):
    datetime = models.DateTimeField(verbose_name='Время события', default=timezone.now)
    action = models.CharField(verbose_name='Действие пользователя', max_length=300)

    def __str__(self):
        return f'{self.datetime.strftime("%d.%m.%Y %H:%M")}: "{self.action}"'
