from django.contrib import admin

from .views import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created', 'updated', 'published')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'content')
    search_fields = ('title', 'id')

admin.site.register(News, NewsAdmin)
