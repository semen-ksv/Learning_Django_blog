# Generated by Django 3.0.7 on 2020-06-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200610_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, default='photos/Article.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
