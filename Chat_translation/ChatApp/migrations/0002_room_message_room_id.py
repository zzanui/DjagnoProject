# Generated by Django 4.1.2 on 2022-12-21 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ManyToManyField(related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'room',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='room_id',
            field=models.ForeignKey(db_column='room_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='ChatApp.room'),
        ),
    ]
