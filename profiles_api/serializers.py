from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView, very similar to Django Forms"""
    name = serializers.CharField(min_length=5, max_length=10)