# Generated by Django 3.1.4 on 2020-12-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201215_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='meta_title',
            field=models.CharField(default=1, max_length=128, verbose_name='Тайтл страницы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seo',
            name='path',
            field=models.CharField(choices=[('/', 'Главная'), ('/coaching', 'О коучинге'), ('/programs', 'Программы'), ('/timetable', 'Распиание'), ('/timetable-filter', 'Распиание'), ('/games', 'Трансформационные игры'), ('/about', 'О нас'), ('/news', 'Новости'), ('/feed-list', 'Отзывы'), ('/coaches', 'Тренеры'), ('/contacts', 'Контакты')], max_length=32, unique=True, verbose_name='Адрес страницы'),
        ),
    ]
