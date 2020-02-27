from rest_framework import serializers
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

#1, permission 序列化器
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

#2, permission contentType序列化器
class PermissionContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ("id","name")