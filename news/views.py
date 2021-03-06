from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News, Category
from .forms import NewsForm, UserRegForm, UserLoginForm
from .serializers import NewsListSerializer, NewsDetailSerializer


def register(request):
    # регистрация нового пользователя

    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have been registered on site!')
            return redirect('home')
        else:
            messages.error(request, 'Error of registration')
    else:
        form = UserRegForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

class HomeNews(ListView):
    """вивод всех новостей, используеться вместо функции index"""
    model = News
    template_name = 'news/index_news.html'
    context_object_name = 'news'
    paginate_by = 3

    # default_img = 'media/photos/Article.jpg'
    # extra_context = {'title': 'All News',
    #                  'article_img': default_img,
    #                  }
    def get_context_data(self, *, object_list=None, **kwargs):
        # лучше использовать вместо extra_context
        context = super(HomeNews, self).get_context_data(**kwargs)
        default_img = 'media/photos/Article.jpg'
        context['title'] = 'All News'
        context['article_img'] = default_img
        return context

    def get_queryset(self):
        # фильтруем вывод новостей на страницу, по галочке публикации
        # используем select_related для вывода всех категорий по одному запросу в базу даных
        return News.objects.filter(published=True).select_related('category')


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


class NewsByCategory(ListView):
    """подбор новостей по категориям с бокового меню, вместо функции get_category"""
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False  # запрещаем показ пустых списков категории, которых нету
    paginate_by = 5

    def get_queryset(self):
        # фильтруем вывод новостей на страницу, по категориям
        return News.objects.filter(category_id=self.kwargs['category_id'], published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['category_id'])
        default_img = '/media/photos/Article.jpg'
        context['article_img'] = default_img
        return context

# def get_category(request, category_id):
#     # подбор новостей по категориям с бокового меню
#     news = News.objects.filter(category_id=category_id)
#     # categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news,
#                                                   'category': category,
#                                                   })


class ViewNews(DetailView):
    """просмотр отдельной новости, используем вместо view_news"""
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'article'

    # pk_url_kwarg = 'pk'
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(ViewNews, self).get_context_data(**kwargs)
    #     context['article'] = get_object_or_404(News, pk=self.kwargs['pk'])
    #     return context

# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'article': news_item})


class CreateNews(LoginRequiredMixin, CreateView):
    """вывод форми для создание новости, вместо функции add_news"""
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'

# def add_news(request):
#     # добавили форму связанную с данными и не связанную
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # article = News.objects.create(**form.cleaned_data)
#             article = form.save()
#             return redirect(article)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})


class NewsListView(APIView):
    """Output list of news"""

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)

class NewsSingleView(APIView):
    """Output detail's of single news"""

    def get(self, request, pk):
        new = News.objects.get(id=pk, published=True)
        serializer = NewsDetailSerializer(new)
        return Response(serializer.data)
