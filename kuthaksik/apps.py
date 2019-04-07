from django.apps import AppConfig


class KuthaksikConfig(AppConfig):
    name = 'kuthaksik'

    def ready(self):
        from haksikUpdater import updater
        updater.start()