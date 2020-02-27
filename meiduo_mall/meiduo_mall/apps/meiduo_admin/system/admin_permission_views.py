from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import admin_permission_serializers
from users.models import User
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import Group


# 1,管理员信息
class AdminPermissionViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = admin_permission_serializers.AdminPermissionSerializer
    queryset = User.objects.filter(is_staff=True, is_superuser=True).all()


# 2,组信息
class GroupPermissionView(ListAPIView):
    serializer_class = admin_permission_serializers.GroupPermissionSerializer
    queryset = Group.objects.all()
