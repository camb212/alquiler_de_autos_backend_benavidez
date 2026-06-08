from rest_framework import viewsets, permissions
from rental.models import User
from rental.serializers.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # El registro es público
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        # Para listar, actualizar o eliminar, debe ser Administrador (Staff)
        if self.action in ['list', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        
        # Para ver perfil propio
        return [permissions.IsAuthenticated()]
