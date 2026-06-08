from rest_framework import serializers
from rental.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "phone", "role"]

    def create(self, validated_data):
        # Aseguramos que la contraseña se guarde de forma segura (hasheada)
        user = User.objects.create_user(**validated_data)
        return user
