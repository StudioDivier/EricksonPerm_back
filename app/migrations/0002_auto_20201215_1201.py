# Generated by Django 3.1.4 on 2020-12-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeds',
            options={'verbose_name': 'Отзывы', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.RemoveField(
            model_name='feeds',
            name='img',
        ),
        migrations.AddField(
            model_name='feeds',
            name='img_detail',
            field=models.ImageField(default=1, upload_to='feeds/', verbose_name='Изображение на странице отзывов'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeds',
            name='img_detail_alt',
            field=models.CharField(default=1, max_length=128, verbose_name='Изображение на странице отзывов (Alt)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeds',
            name='img_main',
            field=models.ImageField(default=1, upload_to='feeds/', verbose_name='Изображение на главной странице'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feeds',
            name='img_main_alt',
            field=models.CharField(default=1, max_length=128, verbose_name='Изображение на главной странице (Alt)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feeds',
            name='description_long',
            field=models.TextField(verbose_name='Описание полное'),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='description_short',
            field=models.TextField(verbose_name='Описание короткое'),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='video_review',
            field=models.URLField(verbose_name='Видео'),
        ),
    ]
