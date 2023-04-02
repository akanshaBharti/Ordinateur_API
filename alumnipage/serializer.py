from rest_framework import serializers
from .models import *

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
