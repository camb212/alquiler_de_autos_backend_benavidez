from django.db import models
from .reservation import Reservation

class Payment(models.Model):
    PAYMENT_METHODS = (
        ("CARD", "Credit/Debit Card"),
        ("CASH", "Cash"),
        ("TRANSFER", "Bank Transfer"),
    )
    
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, default="PAID")
    transaction_id = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for Reservation {self.reservation.id}"
