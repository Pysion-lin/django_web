from rest_framework import serializers
from users.models import User
from django.contrib.auth.models import Group


# 1,管理员序列化器
class AdminPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    #1,重写create方法,密码加密,设置管理员
    def create(self, validated_data):
        #1,创建用户对象
        user = super().create(validated_data)

        #2,设置管理员密码加密
        user.is_superuser = True
        user.is_staff = True
        user.set_password(validated_data["password"])
        user.save()

        #3,返回
        return user

    #2,重写update方法,密码加密
    def update(self, instance, validated_data):
        #1,更新普通信息
        user = super().update(instance,validated_data)

        #2,密码加密
        user.set_password(validated_data["password"])
        user.save()

        #3,返回
        return user

# 2,组序列化器
class GroupPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")
