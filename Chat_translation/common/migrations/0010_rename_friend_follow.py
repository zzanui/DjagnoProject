# Generated by Django 4.1.2 on 2022-11-29 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_friend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Friend',
            new_name='Follow',
        ),
    ]