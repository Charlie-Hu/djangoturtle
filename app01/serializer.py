from app01.models import Userplan
from rest_framework import serializers


class HardwareDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userplan
        fields = ["dosage", "times", "num_time", "email", "name"]
