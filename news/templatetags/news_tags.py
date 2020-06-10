from django import template
from django.db.models import Count

from news.models import Category


register = template.Library()
# позволяет получить все категории напрямую без дублирования в views
@register.simple_tag
def get_all_categories():
    return Category.objects.all()

@register.simple_tag
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return  categories