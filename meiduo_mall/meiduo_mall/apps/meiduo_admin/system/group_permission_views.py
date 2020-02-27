from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from django.contrib.auth.models import Group,Permission
from . import group_permission_serializers
from rest_framework.generics import ListAPIView


#1, group permission 信息
class GroupPermissionViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = group_permission_serializers.GroupPermissionSerializer
    queryset = Group.objects.all()

#2,permission 信息
class PermissionSimpleView(ListAPIView):
    serializer_class = group_permission_serializers.PermissionSimpleSerializer
    queryset = Permission.objects.all()