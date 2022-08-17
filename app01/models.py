from django.db import models


class Userinfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
