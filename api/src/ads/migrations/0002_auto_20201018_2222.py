# Generated by Django 3.1.1 on 2020-10-19 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adcomment',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads_adcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adcomment',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_ads_adcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adcomment',
            name='saved_users',
            field=models.ManyToManyField(blank=True, related_name='saved_ads_adcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adcomment',
            name='tagged_users',
            field=models.ManyToManyField(blank=True, related_name='tagged_ads_adcomment_comment_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='creator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads_ad_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='liked_users',
            field=models.ManyToManyField(blank=True, related_name='liked_ads_ad_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='saved_users',
            field=models.ManyToManyField(blank=True, related_name='saved_ads_ad_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='tagged_users',
            field=models.ManyToManyField(blank=True, related_name='tagged_ads_ad_set', to=settings.AUTH_USER_MODEL),
        ),
    ]