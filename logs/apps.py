from django.apps import AppConfig


class LogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'logs'

    def ready(self) -> None:
        from .containers import CatsContainer

        cats_container = CatsContainer()
        cats_container.wire(['.views'])

        return super().ready()
