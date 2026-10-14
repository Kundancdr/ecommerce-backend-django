from django.urls import path
from .views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]