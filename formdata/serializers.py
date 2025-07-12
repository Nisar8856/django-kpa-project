from rest_framework import serializers
from .models import FormData

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = '__all__'
