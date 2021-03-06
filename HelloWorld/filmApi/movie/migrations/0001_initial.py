# Generated by Django 3.0.5 on 2020-05-05 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField()),
                ('poster', models.ImageField(upload_to='img')),
                ('director', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
            ],
            options={
                'verbose_name': 'movie',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=60)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movie.User')),
            ],
            options={
                'verbose_name': 'user_token',
            },
        ),
    ]
