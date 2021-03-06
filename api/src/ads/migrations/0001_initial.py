# Generated by Django 3.1.1 on 2020-10-19 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(blank=True, max_length=1000)),
                ('region', models.PositiveSmallIntegerField(choices=[(0, 'Waterloo'), (1, 'Toronto'), (2, 'Brampton'), (3, 'Ottawa')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.PositiveSmallIntegerField(choices=[(0, 'Electronics'), (1, 'Books'), (2, 'Food'), (3, 'Other')], default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('postal_code', models.CharField(default='A1B2C3', max_length=6)),
            ],
            options={
                'ordering': ['-datetime_created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=1000)),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='ads.ad')),
            ],
            options={
                'ordering': ['-datetime_created'],
                'abstract': False,
            },
        ),
    ]
