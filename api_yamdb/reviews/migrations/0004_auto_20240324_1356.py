# Generated by Django 3.2 on 2024-03-24 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20240324_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'default_related_name': 'comments', 'ordering': ('pub_date',), 'verbose_name': 'комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'default_related_name': 'reviews', 'ordering': ('pub_date',), 'verbose_name': 'отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
