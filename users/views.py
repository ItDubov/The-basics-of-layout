from django.contrib.auth import login, get_user_model
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegisterForm


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('products:product_list')  # Укажите нужный путь после регистрации

    def form_valid(self, form):
        # Сохраняем пользователя
        user = form.save()

        # Автовход после регистрации
        login(self.request, user)

        # Отправляем приветственное письмо
        send_mail(
            'Добро пожаловать!',
            f'Здравствуйте, {user.email}! Спасибо за регистрацию!',
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )

        return redirect(self.get_success_url())


class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('products:product_list')  # Укажите путь, куда пользователю нужно попасть после входа
