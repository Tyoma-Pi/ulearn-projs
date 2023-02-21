# Generated by Django 4.1.3 on 2022-12-18 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ch_g', '0002_alter_book_dlcount_alter_book_isbn'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditonalUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.TextField(verbose_name='Фотография')),
                ('city', models.TextField(verbose_name='Город')),
                ('about', models.TextField(verbose_name='О себе')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлено в базу')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-published'],
            },
        ),
    ]