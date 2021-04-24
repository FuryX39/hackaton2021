from django.db import models
from datetime import datetime


class User(models.Model):

    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    nfc_code = models.CharField(max_length=255, verbose_name='NFC-код')

    def __str__(self):
        return self.full_name


class Operation(models.Model):

    user = models.ForeignKey(to=User, verbose_name='Пользователь', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=datetime.now, verbose_name='Время и дата операции')
    mass = models.CharField(max_length=255, verbose_name='Масса мусора')
    trash_type = models.CharField(max_length=255, verbose_name='Тип мусора')

    def __str__(self):
        return f'{self.user} - {self.date_time}'


class Trash(models.Model):

    location = models.CharField(max_length=255)
    password = models.CharField(max_length=64, default='literallyHardPassword')

    def __str__(self):
        return self.location
