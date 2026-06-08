from rest_framework import viewsets, permissions
from rental.models import Payment
from rental.serializers.payment_serializer import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
