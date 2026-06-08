from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Lógica para asegurar que los superusuarios siempre sean ADMIN en la app
        user_role = self.user.role
        if self.user.is_staff or self.user.is_superuser:
            user_role = "ADMIN"
            
        return {
            "token": data["access"],
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "role": user_role
            }
        }

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
