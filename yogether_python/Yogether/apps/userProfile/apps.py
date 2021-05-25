from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userProfile'
    verbose_name = 'Пользователи'

    def ready(self):
        import userProfile.signals
