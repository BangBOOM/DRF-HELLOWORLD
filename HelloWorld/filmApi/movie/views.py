from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movie.serializers import *
from rest_framework import viewsets


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = []

    # 普通用户只允许创建账户,使用登录功能
    def get_permissions(self):
        if self.action not in ('create',):
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = []
        return [permission() for permission in self.permission_classes]


class RegisterViewSet(UserViewSet):
    serializer_class = RegSerializers

    def create(self, request, *args, **kwargs):
        res = RegSerializers(data=request.data)
        if res.is_valid():
            res.save()
        return Response(res.errors)


class LogInViewSet(UserViewSet):
    serializer_class = LogSerializers

    def create(self, request, *args, **kwargs):
        data = request.data
        res = LogSerializers(data=data)
        if res.is_valid():
            return Response(res.validated_data)
        return Response(res.errors)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()  # 获取数据库中的所有内容
    serializer_class = MovieSerializer  # 序列化


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers

    def create(self, request, *args, **kwargs):
        data = request.data
        res = CommentSerializers(data=data)
        if res.is_valid():
            res.save()
        return Response(res.errors)
