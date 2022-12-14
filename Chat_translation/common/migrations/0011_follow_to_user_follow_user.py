# Generated by Django 4.1.2 on 2022-12-06 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_rename_friend_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='to_user',
            field=models.ManyToManyField(related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.OneToOneField(default='SOME STRING', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
