from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from.models import Cart
from.serializers import CartSerializer
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers

class CartListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=['Cart'], responses=CartSerializer(many=True))
    def get(self, request):
        items = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(items, many=True)
        return Response(serializer.data)

class CartAddView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Cart'],
        request=inline_serializer('CartAddRequest', {
            'product': serializers.IntegerField(help_text='Product ID'),
            'quantity': serializers.IntegerField(required=False, default=1),
        }),
        responses=CartSerializer,
    )
    def post(self, request):
        product_id = request.data.get('product')
        qty = int(request.data.get('quantity', 1))

        item, created = Cart.objects.get_or_create(
            user=request.user,
            product_id=product_id,
            defaults={'quantity': qty}
        )
        if not created:
            item.quantity += qty
            item.save()

        serializer = CartSerializer(item)
        return Response(serializer.data)

class CartDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['Cart'],
        responses=inline_serializer('CartRemoveResponse', {'message': serializers.CharField()}),
    )
    def delete(self, request, pk):
        Cart.objects.filter(id=pk, user=request.user).delete()
        return Response({"message": "removed"})

# Create your views here.
