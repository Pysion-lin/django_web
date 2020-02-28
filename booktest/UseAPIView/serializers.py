from rest_framework import serializers
from .models import BookInfo

#1,定义模型类序列化器的书籍
class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = "__all__"