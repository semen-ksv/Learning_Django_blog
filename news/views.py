from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from news.models import News


def index(request):
    news = News.objects.all()
    # news = News.objects.order_by('-created')
    defaul_img = 'media/photos/Article.jpg'
    return render(request, 'news/index_news.html', {'news': news, 'title': 'News', 'article_imp': defaul_img})