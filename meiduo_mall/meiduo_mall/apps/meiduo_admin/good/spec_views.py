from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import spec_serializers
from goods.models import SPUSpecification

#1,spec信息
class SpecViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = spec_serializers.SpecViewSetSerializer
    queryset = SPUSpecification.objects.all()