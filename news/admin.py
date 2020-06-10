from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created', 'updated', 'category', 'published')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'published')
    search_fields = ('title', 'id')
    fields = ('title', 'category', 'content', 'views_count', 'get_photo', 'photo', 'created', 'updated', 'published')
    readonly_fields = ('get_photo', 'views_count', 'created', 'updated')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="200">')
        else:
            return 'Photo does\'t exist'


admin.site.register(News, NewsAdmin)
admin.site.register(Category)
