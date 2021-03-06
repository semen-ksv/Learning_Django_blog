from django.urls import path
from news.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('logint/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('api/news/', NewsListView.as_view()),
    path('api/news/<int:pk>/', NewsSingleView.as_view()),
]