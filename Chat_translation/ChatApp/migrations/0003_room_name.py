# Generated by Django 4.1.2 on 2022-12-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0002_room_message_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
