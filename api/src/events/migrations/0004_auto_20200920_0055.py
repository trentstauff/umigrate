# Generated by Django 3.0.6 on 2020-09-20 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200917_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='event',
            name='likes_count',
        ),
        migrations.RemoveField(
            model_name='eventcomment',
            name='likes_count',
        ),
    ]
