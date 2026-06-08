from rest_framework import viewsets, permissions
from rental.models import User
from rental.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # 1. Registro público
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        # 2. Solo el Admin puede ver la lista de todos los usuarios (CRUD)
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        
        # 3. Para ver su propio perfil (retrieve) o editarlo, deben estar logueados
        return [permissions.IsAuthenticated()]
