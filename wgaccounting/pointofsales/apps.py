from django.apps import AppConfig


class PointofsalesConfig(AppConfig):
    name = 'pointofsales'

    def ready(self):
        import pointofsales.signals