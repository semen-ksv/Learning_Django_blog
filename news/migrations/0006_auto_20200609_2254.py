# Generated by Django 3.0.7 on 2020-06-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200609_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, default='photos/Article.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
