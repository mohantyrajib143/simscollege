from website.models import slider
from rest_framework import serializers

class SliderSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()