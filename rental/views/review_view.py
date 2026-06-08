from rest_framework import viewsets, permissions
from rental.models import Review
from rental.serializers.review_serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['vehicle']
