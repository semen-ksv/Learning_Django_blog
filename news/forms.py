from django import forms
from .models import Category, News

class NewsForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "rows": 7}))
    photo = forms.ImageField(required=False)
    published = forms.BooleanField(label='Are publish news ? ', initial=True, )
    category = forms.ModelChoiceField(empty_label='Select category', queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "form-control"}))
