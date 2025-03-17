from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    # Дополнительные поля
    avatar = forms.ImageField(required=False)
    phone = forms.CharField(max_length=20, required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'avatar', 'phone', 'country']

    # Валидатор для email (если необходимо)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
