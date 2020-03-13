# Generated by Django 2.2 on 2020-03-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedSpot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('latitude', models.TextField(default='00000')),
                ('longitude', models.TextField(default='00000')),
            ],
        ),
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('latitude', models.TextField(default='00000')),
                ('longitude', models.TextField(default='00000')),
                ('description', models.TextField(default='00000')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.TimeField(auto_created=True, auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nickname', models.TextField(default='guest')),
                ('email', models.EmailField(default='000000000', max_length=254, unique=True)),
                ('token', models.TextField(default='', null=True, unique=True)),
            ],
        ),
    ]