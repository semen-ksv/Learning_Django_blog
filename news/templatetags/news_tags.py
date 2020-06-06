from django import template
from news.models import Category


register = template.Library()
# позволяет получить все категории напрямую без дублирования в views
@register.simple_tag
def get_all_categories():
    return Category.objects.all()