from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from news.models import News, Category
from .forms import NewsForm


class HemeNews(ListView):
    """вивод всех новостей, используеться вместо функции index"""
    model = News
    template_name = 'news/index_news.html'
    context_object_name = 'news'

    # default_img = 'media/photos/Article.jpg'
    # extra_context = {'title': 'All News',
    #                  'article_img': default_img,
    #                  }
    def get_context_data(self, *, object_list=None, **kwargs):
        # лучше использовать вместо extra_context
        context = super(HemeNews, self).get_context_data(**kwargs)
        default_img = 'media/photos/Article.jpg'
        context['title'] = 'All News'
        context['article_img'] = default_img
        return context

    def get_queryset(self):
        # фильтруем вывод новостей на страницу, по галочке публикации
        return News.objects.filter(published=True)


# def index(request):
#     # вивод всех новостей на шаблоне index
#     news = News.objects.all()
#     # news = News.objects.order_by('-created')
#     default_img = 'media/photos/Article.jpg'
#     # categories = Category.objects.all()
#     return render(request, 'news/index_news.html', {'news': news,
#                                                     'title': 'All News',
#                                                     'article_img': default_img,
#                                                     })


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


def add_news(request):
    # добавили форму связанную с данными и не связанную
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # article = News.objects.create(**form.cleaned_data)
            article = form.save()
            return redirect(article)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
