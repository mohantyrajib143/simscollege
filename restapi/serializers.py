from website.models import slider
from rest_framework import serializers

class SliderSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    status = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    is_active = serializers.CharField()
