# Generated by Django 3.1.1 on 2020-10-19 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=500)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('profile_photo', models.ImageField(blank=True, upload_to='images/message_profile_photos')),
                ('background_photo', models.ImageField(blank=True, upload_to='images/message_background_photos')),
            ],
            options={
                'ordering': ['-datetime_created'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('background_photo', models.ImageField(blank=True, upload_to='images/room_background_photos')),
                ('profile_photo', models.ImageField(blank=True, upload_to='images/room_profile_photos')),
                ('privacy_level', models.IntegerField(choices=[(0, 'Public'), (1, 'Private'), (2, 'Direct Messaging')], default=0)),
            ],
            options={
                'ordering': ['-datetime_created'],
            },
        ),
    ]
