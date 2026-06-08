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
        if instance.is_staff or instance.is_superuser:
            ret['role'] = "ADMIN"
        return ret

    def create(self, validated_data):
        request = self.context.get('request')
        # Solo si quien crea es admin, permitimos asignar el rol ADMIN
        is_request_from_admin = request and request.user and (request.user.is_staff or request.user.is_superuser)
        
        role = validated_data.get('role', 'CLIENT')
        password = validated_data.pop('password', None)
        
        if role == "ADMIN" and is_request_from_admin:
            validated_data['is_staff'] = True
        else:
            validated_data['is_staff'] = False
            validated_data['role'] = 'CLIENT'
            
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        request = self.context.get('request')
        is_request_from_admin = request and request.user and (request.user.is_staff or request.user.is_superuser)
        
        role = validated_data.get('role')
        password = validated_data.pop('password', None)

        # Solo un admin puede cambiar roles
        if is_request_from_admin and role:
            instance.is_staff = (role == "ADMIN")
            instance.role = role
        
        if password:
            instance.set_password(password)
            
        return super().update(instance, validated_data)
