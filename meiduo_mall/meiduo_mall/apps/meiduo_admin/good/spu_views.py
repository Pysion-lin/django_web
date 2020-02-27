from rest_framework.viewsets import ModelViewSet
from goods.models import SPU,Brand,GoodsCategory
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import spu_serializers
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from fdfs_client.client import Fdfs_client
from django.conf import settings

#1,spu信息
class SPUViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = spu_serializers.SPUViewSetSerializer
    queryset = SPU.objects.all()

#2,spu,品牌信息
class SPUBrandSimpleView(ListAPIView):
    serializer_class = spu_serializers.SPUBrandSimpleSerializer
    queryset = Brand.objects.all()

#3,spu, 一级分类
class SPUCategoryView(ListAPIView):
    serializer_class = spu_serializers.SPUCategorySerializer
    queryset = GoodsCategory.objects.filter(parent=None).all()

#4, spu,二级,三级分类
class SPUCategorySubView(ListAPIView):
    serializer_class = spu_serializers.SPUCategorySerializer

    def get_queryset(self):
        #1,获取分类编号
        category_id = self.kwargs.get("category_id")

        #2,获取子分类
        return GoodsCategory.objects.get(id=category_id).subs.all()

#5, 图片上传
class SPUImageUploadView(APIView):
    def post(self,request):
        #1,获取参数
        image = request.FILES.get("image")

        #2,校验参数
        if not image:
            return Response(status=400)

        #3,入库(fdfs)
        client = Fdfs_client(settings.FDFS_CONFIG)
        ret = client.upload_by_buffer(image.read())

        if ret["Status"] != "Upload successed.":
            return Response(status=400)

        #4,返回响应
        return Response({
            "img_url": settings.BASE_URL + ret.get("Remote file_id")
        })