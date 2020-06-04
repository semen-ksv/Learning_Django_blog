from django.db import models

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
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')
    published = models.BooleanField(default=True)