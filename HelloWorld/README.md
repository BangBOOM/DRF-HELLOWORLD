# VUE+DRF
Vue.js和Django Rest Framework的前后端分离开发的一个HelloWorld


## 启动

后端项目使用PyCharm开发，前端项目使用WebStorm开发。

首先启动后台项目切换到filmApi文件夹下面，打开终端输入
```
首先确保python使用的3.8

pip install -r requirements.txt # 安装依赖

python manage.py runserver
```

前端项目启动需要npm，相关内容百度
切换到film_online下面,打开终端输入下面这两个句启动前端
```
npm install

npm run serve
```

打开网页结果
![](imgs\demo.jpg)



## 第一步创建Django项目
与一般的Django项目创建不同的是在setting中需要添加上`rest_framework`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # this place
]
```

##  创建APP

+ 首先在{appname}/model.py中新建表

```
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
```
+ 接着在{appname}文件下新建`serializers.py`文件用于将表序列化，换句话说就是查询数据库得到的数据是字典格式`{name:'xxx',info:'xxx'}`将其转换成json格式的数据，发送给前端，方便前端解析。

```
from rest_framework import serializers
from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'    #数据表中的所有字段
```

+ 编辑`views.py`文件这个文件负责一般负责前端页面渲染，但是这里只担任数据提交的工作,具体的方法都在继承的类中，这里先不展开。

```
from movie.models import Movie
from movie.serializers import MovieSerializer

from rest_framework import viewsets
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()  # 获取数据库中的所有内容
    serializer_class = MovieSerializer  # 序列化
```

+ 修改{appname}文件下的`urls.py`文件添加路由

```
from movie import views
from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

app_name='movie'

router=DefaultRouter()
router.register(r'movie',views.MovieViewSet)

urlpatterns=[
    url(r'^api/',include(router.urls)),
]
```

+ 在{appname}\admin.py中注册model,目的是使用django自带的后台管理来修改数据
```
admin.site.register(Movie)
```

## 创建vue-cli

使用`vue create xxxx`创建前端项目项目

这部分后续再写就是用axios获取后台的链接。


## 前后项目连接

目前前端项目还无法访问后端内容因为跨域访问，前端项目开启是8080端口，后端是8000端口，
需要在django项目的setting文件中再添加上这些内容

```
# 可以直接把源文件中的这个和下面这个替换
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    # add this
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True        #add this

```