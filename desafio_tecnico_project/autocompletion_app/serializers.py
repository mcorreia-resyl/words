from dataclasses import fields
from rest_framework import serializers
from .models import Words
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'