from django.shortcuts import render, get_object_or_404
from news.models import News, Category


def index(request):
    # вивод всех новостей на шаблоне index
    news = News.objects.all()
    # news = News.objects.order_by('-created')
    default_img = 'media/photos/Article.jpg'
    # categories = Category.objects.all()
    return render(request, 'news/index_news.html', {'news': news,
                                                    'title': 'All News',
                                                    'article_img': default_img,
                                                    })


def get_category(request, category_id):
    # подбор новостей по категориям с бокового меню
    news = News.objects.filter(category_id=category_id)
    # categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,
                                                  'category': category,
                                                  })

def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'article': news_item})