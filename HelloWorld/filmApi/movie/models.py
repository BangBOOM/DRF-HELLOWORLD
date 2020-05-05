from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)

    # 电影名称
    name = models.CharField(max_length=50)

    # 电影简介
    info = models.TextField()

    # 电影海报
    poster = models.ImageField(upload_to='img')

    # 电影导演
    director = models.CharField(max_length=50)

    # 电影时长
    duration = models.IntegerField()

    class Meta:
        verbose_name = "movie"

    def __str__(self):
        return self.name

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)

    class Meta:
        verbose_name="user"

class UserToken(models.Model):
    username=models.OneToOneField(to='User',on_delete=models.CASCADE)
    token=models.CharField(max_length=60)

    class Meta:
        verbose_name="user_token"
