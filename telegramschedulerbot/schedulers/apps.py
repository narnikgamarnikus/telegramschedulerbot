from django.apps import AppConfig


class SchedulersConfig(AppConfig):
    name = 'telegramschedulerbot.schedulers'
    verbose_name = "Schedulers"

    def ready(self):
        pass
        #import telegramschedulerbot.schedulers.tasks