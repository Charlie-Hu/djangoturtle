from django.db import models


class Userinfo(models.Model):
    name = models.CharField(verbose_name="account_number", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)
