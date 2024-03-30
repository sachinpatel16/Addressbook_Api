from rest_framework import serializers
from api.models import Addres


class AddresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addres
        fields = '__all__'