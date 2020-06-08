from django.db import models
from django.urls import reverse

# Create your models here.
class News(models.Model):
    """
    Table with posts of news

    CREATE TABLE "news_news" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                            "title" varchar(200) NOT NULL UNIQUE,
                            "content" text NOT NULL,
                            "created" datetime NOT NULL,
                            "updated" datetime NOT NULL,
                            "photo" varchar(100) NOT NULL,
                            "published" bool NOT NULL);
    """

    title = models.CharField(max_length=200, unique=True)
    # для названия полей на русском добавить verbose_name = "Новость"
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        # создаем ссылки для категорий для перехода и указания в html
        return reverse('view_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = 'News'
        ordering = ['-created', 'title']


class Category(models.Model):
    category_title = models.CharField(max_length=150, db_index=True)

    def get_absolute_url(self):
        # создаем ссылки для категорий для перехода и указания в html
        return reverse('category', kwargs={'category_id': self.pk})


    def __str__(self):
        return f'{self.category_title}'

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Category'
        ordering = ['category_title']