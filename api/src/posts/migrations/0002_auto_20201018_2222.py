# Generated by Django 3.1.1 on 2020-10-19 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_postcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_posts_postcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='posts.post'),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='saved_users',
            field=models.ManyToManyField(blank=True, related_name='saved_posts_postcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postcomment',
            name='tagged_users',
            field=models.ManyToManyField(blank=True, related_name='tagged_posts_postcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts_post_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_posts_post_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='saved_users',
            field=models.ManyToManyField(blank=True, related_name='saved_posts_post_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='tagged_users',
            field=models.ManyToManyField(blank=True, related_name='tagged_posts_post_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
