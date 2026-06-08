from rest_framework import viewsets, permissions
from rental.models import Reservation
from rental.serializers.reservation_serializer import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == "ADMIN":
            return Reservation.objects.all()
        return Reservation.objects.filter(user=user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            # Solo el Admin o el dueño (si implementamos lógica de dueño) pueden borrar/editar
            # Por simplicidad, permitimos a usuarios autenticados y filtramos el queryset
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        # Si un cliente crea una reserva, nos aseguramos de que sea para él mismo
        if not (self.request.user.is_staff or self.request.user.is_superuser or self.request.user.role == "ADMIN"):
            serializer.save(user=self.request.user)
        else:
            serializer.save()
