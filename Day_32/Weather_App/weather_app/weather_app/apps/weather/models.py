from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        """
        Метакласс. Позволяет добавить данные о самой модели.
        """
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


# INSTRUCTION:
# добавить в apps.py класс WeatherConfig(AppConfig)
# утановить в settings.py INSTALLED_APPS = ['weather.apps.WeatherConfig',]
# выполнить python manage.py makemigrations weather
# выполнить python manage.py migrate