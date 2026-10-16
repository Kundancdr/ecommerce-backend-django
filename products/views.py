from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from.models import Category, Product
from.serializers import CategorySerializer, ProductSerializer
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(get=extend_schema(tags=['Categories']), post=extend_schema(tags=['Categories']))
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

@extend_schema_view(get=extend_schema(tags=['Products']), post=extend_schema(tags=['Products']))
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]