from rest_framework import viewsets

from rental.models import Reservation
from rental.serializers.reservation_serializer import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer