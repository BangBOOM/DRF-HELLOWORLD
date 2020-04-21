from movie.models import Movie
from movie.serializers import MovieSerializer

from rest_framework import viewsets
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()  # 获取数据库中的所有内容
    serializer_class = MovieSerializer  # 序列化
