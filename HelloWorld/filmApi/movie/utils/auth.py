"""
author:Wenquan Yang
time:2020/5/6 1:41
"""
from rest_framework import exceptions
from movie import models
from rest_framework.authentication import BaseAuthentication


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        token=request._request.GET.get('token')
        token_obj=models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.username,token_obj)
