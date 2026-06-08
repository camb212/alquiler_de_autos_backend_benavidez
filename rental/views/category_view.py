from rest_framework import viewsets

from rental.models import Category
from rental.serializers.category_serializer import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer