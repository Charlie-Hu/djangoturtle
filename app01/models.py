from django.db import models


class Userplan(models.Model):
    name = models.CharField(verbose_name="account_number", max_length=32)
    medicine_name = models.CharField(verbose_name='medicine name', max_length=64, blank=True)
    dosage = models.CharField(verbose_name='medicine dosage', max_length=32, blank=True)
    times = models.IntegerField(verbose_name='times', blank=True)
    num_time = models.CharField(verbose_name='time', max_length=256, blank=True)
    email = models.EmailField(verbose_name='emergency email', blank=True)
