from .models import Order
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class':
                                                                                                   'form-control'}))
    captcha = ReCaptchaField()


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField()


class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    captcha = ReCaptchaField()



class OrderCreateForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    vk_or_telegram = forms.CharField(label='Введите ссылку на vk или telegram для связи с админом',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    captcha = ReCaptchaField()



    class Meta:
        model = Order
        fields = ('username', 'email', 'vk_or_telegram')

