from rest_framework import serializers
from rental.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    role = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email", "phone", "role"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Forzamos que la app vea "ADMIN" si el usuario tiene permisos de staff
        if instance.is_staff or instance.is_superuser:
            ret['role'] = "ADMIN"
        return ret

    def create(self, validated_data):
        role = validated_data.get('role', 'CLIENT')
        password = validated_data.pop('password', None)
        
        # Si el rol es ADMIN, le damos permisos de staff
        if role == "ADMIN":
            validated_data['is_staff'] = True
            
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        role = validated_data.get('role')
        password = validated_data.pop('password', None)

        if role:
            instance.is_staff = (role == "ADMIN")
        
        if password:
            instance.set_password(password)
            
        return super().update(instance, validated_data)
