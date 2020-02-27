from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Permission
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import permission_serializers
from rest_framework.generics import ListAPIView
from django.contrib.contenttypes.models import ContentType


#1,permission 信息
class PermissionViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = permission_serializers.PermissionSerializer
    queryset = Permission.objects.order_by("id").all()

#2,permission contentType
class PermissionContentTypeView(ListAPIView):
    serializer_class = permission_serializers.PermissionContentTypeSerializer
    queryset = ContentType.objects.all()
