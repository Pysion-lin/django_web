from rest_framework.viewsets import ModelViewSet
from goods.models import SKU,GoodsCategory,SPU,SPUSpecification
from . import sku_serializers
from meiduo_admin.my_paginate import MyPageNumberPagination
from rest_framework.generics import ListAPIView

#1,sku视图
class SKUViewSet(ModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = sku_serializers.SKUViewSetSerializer
    # queryset = SKU.objects.all()

    #1,重写get_queryset方法
    def get_queryset(self):
        #1,获取过滤关键字
        keyword = self.request.query_params.get("keyword")

        #2,判断关键字
        if keyword:
            return SKU.objects.filter(name__contains=keyword).all()
        else:
            return SKU.objects.all()

#2,sku商品分类(三级分类)
class SKUCategoryView(ListAPIView):
    serializer_class = sku_serializers.SKUCategorySerializer
    queryset = GoodsCategory.objects.filter(subs=None).all()

#3, sku商品简要信息
class SKUGoodSimpleView(ListAPIView):
    serializer_class = sku_serializers.SKUGoodSimpleSerializer
    queryset = SPU.objects.all()

#4, sku,的商品规格信息
class SKUGoodsSpecsView(ListAPIView):
    serializer_class = sku_serializers.SKUGoodsSpecsSerializer
    # queryset = SPUSpecification.objects.all()

    def get_queryset(self):
        #1,获取参数
        spu_id = self.kwargs.get("spu_id")

        #2,查询规格
        return SPUSpecification.objects.filter(spu_id=spu_id).all()