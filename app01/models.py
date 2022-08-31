from django.db import models


class Userinfo(models.Model):
    name = models.CharField(verbose_name="account_number", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)


class Userplan(models.Model):
    medicine_name = models.CharField(verbose_name='medicine name', max_length=64, blank=True)
    dosage = models.CharField(verbose_name='medicine dosage', max_length=32, blank=True)
    times = models.IntegerField(verbose_name='times', blank=True)
    num_time = models.TimeField(verbose_name='time', blank=True)
    email = models.EmailField(verbose_name='emergency email', blank=True)
