from django.apps import AppConfig
# from django.core.signals import request_finished


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        import users.signals

        # Explicitly connect a signal handler.
        # from users.signals import create_profile

        # request_finished.connect(create_profile)
