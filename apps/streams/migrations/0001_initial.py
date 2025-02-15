# Generated by Django 5.0.7 on 2024-07-30 14:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название стрима')),
                ('description', models.TextField(verbose_name='Описание стрима')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('live', models.BooleanField(default=False, verbose_name='В эфире')),
                ('live_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на стрим')),
                ('viewers', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_streams', to='games.games')),
                ('streamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_streams', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Стрим',
                'verbose_name_plural': 'Стримы',
            },
        ),
        migrations.CreateModel(
            name='Clip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название клипа')),
                ('description', models.TextField(verbose_name='Описание клипа')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('clip_url', models.URLField(verbose_name='Ссылка на клип')),
                ('streamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_clips', to=settings.AUTH_USER_MODEL)),
                ('stream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stream_clips', to='streams.stream')),
            ],
            options={
                'verbose_name': 'Клип',
                'verbose_name_plural': 'Клипы',
            },
        ),
    ]
