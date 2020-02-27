from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from meiduo_admin.my_paginate import MyPageNumberPagination
from orders.models import OrderInfo
from . import order_serializers
from rest_framework.response import Response
from rest_framework.decorators import action


#1,order 信息
class OrderViewSet(ReadOnlyModelViewSet):
    pagination_class = MyPageNumberPagination
    serializer_class = order_serializers.OrderViewSetSerializer
    # queryset = OrderInfo.objects.all()

    #1,重写queryset方法
    def get_queryset(self):
        #1,获取参数
        keyword = self.request.query_params.get("keyword","")

        #2,返回结果
        return OrderInfo.objects.filter(order_id__contains=keyword).all()

    #1,重写get_serializerclass方法,返回不同的序列化器
    def get_serializer_class(self):
        if self.action == "retrieve":
            return order_serializers.OrdersModelSerializer
        else:
            return order_serializers.OrderViewSetSerializer

    #2,修改订单状态
    @action(methods=['put'],detail=True) # 格式: orders/pk/status
    def status(self,request,pk):
        #1,获取参数
        status = request.data.get("status")
        order = self.get_object()

        #2,校验参数
        if not all([status,order]):
            return Response(status=403)

        #3,数据入库
        order.status = status
        order.save()

        #4,返回响应
        return Response(status=201)