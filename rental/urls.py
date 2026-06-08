from rest_framework.routers import DefaultRouter

from rental.views.category_view import CategoryViewSet
from rental.views.vehicle_view import VehicleViewSet
from rental.views.reservation_view import ReservationViewSet

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("vehicles", VehicleViewSet)
router.register("reservations", ReservationViewSet)

urlpatterns = router.urls