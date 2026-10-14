from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cart.models import Cart
from.models import Order, OrderItem
from.serializers import OrderSerializer

class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"error": "cart empty hai"}, status=400)

        total = 0
        for item in cart_items:
            total += item.product.price * item.quantity

        order = Order.objects.create(user=request.user, total_price=total)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class MyOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

import razorpay
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

class CreatePaymentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id, user=request.user)
            razorpay_order = client.order.create({
                "amount": int(order.total_price * 100), # paise me
                "currency": "INR",
                "receipt": f"order_{order.id}"
            })
            order.razorpay_order_id = razorpay_order['id']
            order.save()
            return Response({"razorpay_order_id": razorpay_order['id'], "key": settings.RAZORPAY_KEY_ID, "amount": order.total_price})
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

class VerifyPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': data['razorpay_order_id'],
                'razorpay_payment_id': data['razorpay_payment_id'],
                'razorpay_signature': data['razorpay_signature']
            })
            order = Order.objects.get(razorpay_order_id=data['razorpay_order_id'])
            order.is_paid = True
            order.razorpay_payment_id = data['razorpay_payment_id']
            order.razorpay_signature = data['razorpay_signature']
            order.save()
            return Response({"status": "Payment Successful"})
        except Exception as e:
            return Response({"status": "Payment Failed", "error": str(e)}, status=400)