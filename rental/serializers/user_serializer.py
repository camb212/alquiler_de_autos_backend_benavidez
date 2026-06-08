from rest_framework import serializers
from rental.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "phone", "role"]

    def get_role(self, obj):
        # Si el usuario tiene permisos de staff o superusuario en Django, 
        # siempre lo tratamos como ADMIN en la aplicación móvil.
        if obj.is_staff or obj.is_superuser:
            return "ADMIN"
        return obj.role

    def create(self, validated_data):
        # Aseguramos que la contraseña se guarde de forma segura
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
