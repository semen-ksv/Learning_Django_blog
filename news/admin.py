from django.contrib import admin

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created', 'updated', 'category', 'published')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'content')
    search_fields = ('title', 'id')



admin.site.register(News, NewsAdmin)
admin.site.register(Category)