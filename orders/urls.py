from django.urls import path
from.views import CreateOrderView, MyOrdersView

urlpatterns = [
    path('create/', CreateOrderView.as_view()),
    path('my/', MyOrdersView.as_view()),
    path('pay/<int:order_id>/', CreatePaymentView.as_view()),
    path('verify/', VerifyPaymentView.as_view()),
]