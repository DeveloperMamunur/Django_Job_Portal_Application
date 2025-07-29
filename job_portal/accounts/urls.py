from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.forms import CustomLoginForm
from accounts import views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form = CustomLoginForm ), name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]