# Generated by Django 3.2.16 on 2024-03-20 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240320_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Admin', 'Admin'), ('Moderator', 'Moderator')], default='User', max_length=50, verbose_name='Роль'),
        ),
    ]
