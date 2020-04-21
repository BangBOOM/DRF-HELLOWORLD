"""
author:Wenquan Yang
time:2020/4/21 22:16
"""
from rest_framework import serializers
from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'    #数据表中的所有字段

