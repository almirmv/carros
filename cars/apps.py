from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # ao inicializar a app cars importa o signals
    def ready(self):
        import cars.signals        