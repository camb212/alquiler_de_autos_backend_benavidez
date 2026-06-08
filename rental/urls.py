from django.urls import path
from rest_framework.routers import DefaultRouter

from rental.views.category_view import CategoryViewSet
from rental.views.vehicle_view import VehicleViewSet
from rental.views.reservation_view import ReservationViewSet
from rental.views.user_view import UserViewSet
from rental.views.auth_view import LoginView

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("vehicles", VehicleViewSet)
router.register("reservations", ReservationViewSet)
router.register("users", UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
] + router.urls
