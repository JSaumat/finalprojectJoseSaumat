from django.apps import AppConfig

# Configures the forum app in Django
class ForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
