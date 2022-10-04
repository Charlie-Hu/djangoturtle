from app01.models import Userplan
from django.contrib.auth.models import User
from rest_framework import serializers


class HardwareDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userplan
        fields = ["dosage", "times", "num_time"]
