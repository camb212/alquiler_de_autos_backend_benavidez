from django.contrib import admin
from .models import User, Category, Vehicle, Reservation, Payment, Review

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "is_staff")
    list_filter = ("role", "is_staff")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "plate", "price_per_day", "available")
    list_filter = ("available", "category")
    search_fields = ("brand", "model", "plate")

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "vehicle", "start_date", "end_date", "status")
    list_filter = ("status", "start_date")

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "reservation", "amount", "payment_method", "status")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "user", "rating")
