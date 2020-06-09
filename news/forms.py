from django import forms
from django.core.exceptions import ValidationError
from .models import Category, News
import re

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
        if re.match('\d', title):
            raise ValidationError('Название не должно начинаться с цифры!')
        return title
