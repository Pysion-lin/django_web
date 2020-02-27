from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import spec_options_serializers
from goods.models import SpecificationOption,SPUSpecification
from rest_framework.generics import ListAPIView

#1,spec option 信息
class SpecOptionsViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = spec_options_serializers.SpecOptionsViewSetSerializer
    queryset = SpecificationOption.objects.all()

#2,spec 信息
class OptionSpecView(ListAPIView):
    serializer_class = spec_options_serializers.OptionSpecSerializer
    # queryset = SPUSpecification.objects.all()

    #1,重写数据源
    def get_queryset(self):
        queryset = SPUSpecification.objects.all()
        for spec in queryset:
            spec.name = "{}-{}".format(spec.spu.name,spec.name)
        return queryset