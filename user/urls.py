from django.urls import path
from .views.Auth import SignupView, LoginView, SellerLogin

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('seller-login/', SellerLogin.as_view(), name='seller-login'),
]
