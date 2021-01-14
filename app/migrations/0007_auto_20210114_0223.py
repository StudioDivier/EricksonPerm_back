# Generated by Django 3.1.4 on 2021-01-14 02:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210114_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='text',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seo',
            name='path',
            field=models.CharField(choices=[('/', 'Главная'), ('/coaching', 'О коучинге'), ('/programs', 'Программы'), ('/timetable', 'Распиание'), ('/timetable-filter', 'Распиание'), ('/games', 'Трансформационные игры'), ('/about', 'О нас'), ('/article', 'Статьи'), ('/feed-list', 'Отзывы'), ('/coaches', 'Тренеры'), ('/contacts', 'Контакты')], max_length=32, unique=True, verbose_name='Адрес страницы'),
        ),
    ]