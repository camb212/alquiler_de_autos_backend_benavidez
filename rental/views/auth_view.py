from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Adaptamos la respuesta al formato que espera la app Kotlin
        return {
            "token": data["access"],
            "user": {
                "id": self.user.id,
                "username": self.user.username,
                "role": getattr(self.user, 'role', 'CLIENT')
            }
        }

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
