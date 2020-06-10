from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Category, News
import re


class UserRegForm(UserCreationForm):
    """registration form"""
    username = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


# class NewsForm(forms.Form):
#     # форма не связаная с моделями, код дублируеться это минус
#     title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 7}))
#     photo = forms.ImageField(required=False)
#     published = forms.BooleanField(label='Are publish news ? ', initial=True, )
#     category = forms.ModelChoiceField(empty_label='Select category', queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={"class": "form-control"}))


class NewsForm(forms.ModelForm):
    # форма связаная с моделями

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'published', 'category']
        widgets = {'title': forms.TextInput(attrs={"class": "form-control"}),
                   'content': forms.Textarea(attrs={"class": "form-control", "rows": 7}),
                   'category': forms.Select(attrs={"class": "form-control"}),
                   }

    def clean_title(self):
        # кастомная валидация формы для названия

        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры!')
        return title
