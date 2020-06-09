from django.urls import path
from news.views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>', view_news, name='view_news'),
    path('news/add_news', add_news, name='add_news')
]