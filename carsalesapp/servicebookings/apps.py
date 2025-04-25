from django.apps import AppConfig


class ServicebookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servicebookings'

    def ready(self):
       import servicebookings.signals