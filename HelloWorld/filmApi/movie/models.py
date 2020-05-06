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
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        verbose_name = "user"

    def __str__(self):
        return self.username


class UserToken(models.Model):
    username = models.OneToOneField(to='User', on_delete=models.CASCADE)
    token = models.CharField(max_length=60)

    class Meta:
        verbose_name = "user_token"


class Comment(models.Model):
    score = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    comment_id = models.AutoField(primary_key=True) # 评论id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # 用户id
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE) # 电影id
    user_score = models.IntegerField(choices=score, default=3)  # 用户评分
    comment_date = models.DateField(auto_now=True)  # 评论日期
    comment_content=models.TextField(max_length=140)    # 用户评论