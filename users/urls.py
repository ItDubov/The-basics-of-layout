from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),  # Авторизация
    path('logout/', auth_views.LogoutView.as_view(next_page='users:login'), name='logout'),  # Выход
]
