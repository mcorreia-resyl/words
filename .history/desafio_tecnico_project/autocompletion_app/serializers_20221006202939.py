from rest_framework import serializers

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = 