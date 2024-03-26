# Generated by Django 3.2 on 2024-03-25 17:57

from django.db import migrations, models
import users.validation


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True, validators=[users.validation.validate_username], verbose_name='Имя пользователя'),
        ),
    ]
