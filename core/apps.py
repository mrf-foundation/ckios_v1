from django.apps import AppConfig
from apps.hello_world.apps import HelloWorldConfig



class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    label = 'core'