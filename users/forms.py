from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'full_name',
            'phone',
            'city',
            'brith_date',
            'password1',
            'password2'
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'To‘liq ism'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqam'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shahar'
            }),
            'brith_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parol'
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Parolni tasdiqlang'
        })
    )
