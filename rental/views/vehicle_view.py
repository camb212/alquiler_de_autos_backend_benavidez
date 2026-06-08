from rest_framework import viewsets

from rental.models import Vehicle
from rental.serializers.vehicle_serializer import VehicleSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer