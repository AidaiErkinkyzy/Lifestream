# Generated by Django 5.0.7 on 2024-07-30 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название игры')),
                ('description', models.TextField(verbose_name='Описание игры')),
                ('image', models.ImageField(upload_to='games/', verbose_name='Изображение игры')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('download_count', models.PositiveIntegerField(default=0, verbose_name='Количество скачиваний')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Текущие зрители')),
                ('rating', models.FloatField(default=0.0, verbose_name='Рейтинг игры')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.category')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
    ]
