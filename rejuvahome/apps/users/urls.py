from django.urls import path, include
from django.contrib.auth.views import LogoutView

from .views import LoginView, RegisterView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]