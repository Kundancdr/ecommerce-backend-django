from django.urls import path
from .views import CartListView, CartAddView, CartDeleteView

urlpatterns = [
    path('', CartListView.as_view()),
    path('add/', CartAddView.as_view()),
    path('remove/<int:pk>/', CartDeleteView.as_view()),
]