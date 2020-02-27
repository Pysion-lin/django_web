from rest_framework import serializers
from django.contrib.auth.models import Group,Permission

#1,permission group
class GroupPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

#2,permission 序列化器
class PermissionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("id","name")