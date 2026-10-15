# from django.urls import path
# from.views import CreateOrderView, MyOrdersView

# urlpatterns = [
#     path('create/', CreateOrderView.as_view(), name='create-order'),
#     path('my/', MyOrdersView.as_view(), name='my-orders'),
#     path('pay/<int:order_id>/', CreatePaymentView.as_view(), name='create-payment'),
#     path('verify/', VerifyPaymentView.as_view(), name='verify-payment'),
# ]


from django.urls import path
from .views import CreateOrderView, MyOrdersView

urlpatterns = [
    path('create/', CreateOrderView.as_view()),
    path('my/', MyOrdersView.as_view()),
]