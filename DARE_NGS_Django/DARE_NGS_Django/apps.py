from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "DARE_NGS_Django"

    def ready(self):
        import_module("DARE_NGS_Django.receivers")
