from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from.models import Category, Product
from.serializers import CategorySerializer, ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]