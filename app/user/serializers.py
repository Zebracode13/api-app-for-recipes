from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializes for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'wirte_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Creats a new user with encryped password and returns it"""
        return get_user_model().objects.create_user(**validated_data)
