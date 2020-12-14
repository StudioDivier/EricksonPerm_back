# Generated by Django 3.1.4 on 2020-12-14 13:35

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='feeds/')),
                ('title', models.CharField(max_length=128)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('video_review', models.URLField()),
            ],
            options={
                'verbose_name': 'Feed',
                'verbose_name_plural': 'Feeds',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='news/', verbose_name='Изображение новости')),
                ('img_alt', models.CharField(max_length=32, verbose_name='alt изображение')),
                ('date', models.DateField(verbose_name='Дата')),
                ('title', models.CharField(max_length=128, verbose_name='Загаловок')),
                ('description', models.CharField(max_length=256, verbose_name='Описание')),
                ('keywords_seo', models.CharField(max_length=1024, verbose_name='Ключевые слова для СЕО')),
                ('description_seo', models.CharField(max_length=2048, verbose_name='Описание для СЕО')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('form', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
        ),
        migrations.CreateModel(
            name='ProgramOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
            ],
            options={
                'verbose_name': 'ProgramOffer',
                'verbose_name_plural': 'ProgramOffers',
            },
        ),
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(choices=[('/', 'Главная'), ('/coaching', 'О коучинге'), ('/programs', 'Программы'), ('/timetable', 'Распиание'), ('/about', 'О нас'), ('/news', 'Новости'), ('/feed-list', 'Отзывы'), ('/coaches', 'Тренеры'), ('/contacts', 'Контакты')], max_length=32, unique=True, verbose_name='Адрес страницы')),
                ('title', models.CharField(max_length=128, verbose_name='Титульник страницы')),
                ('keywords', models.CharField(max_length=1024, verbose_name='Ключевые слова')),
                ('description', models.CharField(max_length=2048, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'СЕО страницы',
                'verbose_name_plural': 'СЕО страниц',
            },
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='coach_detail/')),
            ],
            options={
                'verbose_name': 'Trainer',
                'verbose_name_plural': 'Trainers',
            },
        ),
        migrations.CreateModel(
            name='WayCouch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way_t', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Направление коуча',
                'verbose_name_plural': 'Направления коучинга',
            },
        ),
        migrations.CreateModel(
            name='WayWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(max_length=64)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trainers')),
            ],
            options={
                'verbose_name': 'WayWork',
                'verbose_name_plural': 'WayWork',
            },
        ),
        migrations.CreateModel(
            name='Timetables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_day', models.IntegerField()),
                ('date_month', models.CharField(max_length=64)),
                ('date_full', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('long', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=128)),
                ('description_short', models.TextField()),
                ('price', models.CharField(max_length=16)),
                ('way', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.waycouch')),
            ],
            options={
                'verbose_name': 'Timetable',
                'verbose_name_plural': 'Timetables',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('title_short', models.CharField(max_length=64, null=True)),
                ('img', models.ImageField(upload_to='games/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description_short', models.TextField()),
                ('date_day', models.IntegerField(null=True)),
                ('date_month', models.IntegerField(null=True)),
                ('date_year', models.IntegerField(null=True)),
                ('long', models.CharField(max_length=64, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(null=True)),
                ('couch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trainers')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_exp', models.IntegerField()),
                ('title_exp', models.CharField(max_length=256)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trainers')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_ed', models.IntegerField()),
                ('end_ed', models.IntegerField()),
                ('ed_title', models.CharField(max_length=256)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.trainers')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
    ]
