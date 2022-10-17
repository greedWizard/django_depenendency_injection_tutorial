from .models import EventLog

from dataclasses import dataclass

from logging import Logger, INFO


@dataclass
class EventLogService:
    logger: Logger

    def create_log(self, action: str) -> EventLog:
        self.logger.info(f"User's activity: {action}")
        EventLog.objects.create(action=action)
