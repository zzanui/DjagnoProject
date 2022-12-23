# Generated by Django 4.1.2 on 2022-12-06 04:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_remove_follow_to_user_follow_to_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='to_users',
        ),
        migrations.AddField(
            model_name='follow',
            name='to_user',
            field=models.ManyToManyField(related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]