from rest_framework.viewsets import ModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from . import sku_images_serializers
from goods.models import SKUImage,SKU
from rest_framework.response import Response
from fdfs_client.client import Fdfs_client
from django.conf import settings

#1,spec option 信息
class SKUImageViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = sku_images_serializers.SKUImageViewSetSerializer
    queryset = SKUImage.objects.all()

    #1,获取所有的sku信息
    def simple(self,request):

        #1,查询所有的sku对象
        skus = SKU.objects.all()

        #2,获取序列化器
        serializer = sku_images_serializers.SKUSerializer(instance=skus,many=True)

        #3,返回响应
        return Response(serializer.data)


    #2,重写create方法
    def create(self, request, *args, **kwargs):
        #1,获取参数
        image = request.FILES.get("image")
        sku_id = request.data.get("sku")

        #2,校验参数
        if not all([image,sku_id]):
            return Response(status=403)

        #3,数据入库
        client = Fdfs_client(settings.FDFS_CONFIG)
        ret = client.upload_by_buffer(image.read())

        #3,1判断是否成功
        if ret["Status"] != "Upload successed.":
            return Response(status=400)

        #3,2数据入库图片
        image_url = ret.get("Remote file_id")
        SKUImage.objects.create(sku_id=sku_id,image=image_url)
        SKU.objects.filter(id=sku_id,default_image_url='').update(default_image_url=image_url)

        #4,返回响应
        return Response(status=201)

    #3,重写update方法
    def update(self, request, *args, **kwargs):
        # 1,获取参数
        image = request.FILES.get("image")
        sku_id = request.data.get("sku")
        sku_image = self.get_object()

        # 2,校验参数
        if not all([image, sku_id]):
            return Response(status=403)

        # 3,数据入库
        client = Fdfs_client(settings.FDFS_CONFIG)
        ret = client.upload_by_buffer(image.read())

        # 3,1判断是否成功
        if ret["Status"] != "Upload successed.":
            return Response(status=400)

        # 3,2数据入库图片
        image_url = ret.get("Remote file_id")
        SKUImage.objects.filter(id=sku_image.id).update(sku_id=sku_id,image=image_url)

        # 4,返回响应
        return Response(status=201)