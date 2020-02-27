from rest_framework.generics import ListAPIView,CreateAPIView
from users.models import User
from . import user_serializers
from meiduo_admin.my_paginate import MyPageNumberPagination
from rest_framework.mixins import CreateModelMixin

class UserView(ListAPIView,CreateAPIView):
    pagination_class = MyPageNumberPagination
    serializer_class = user_serializers.UserSerializer
    # queryset = User.objects.order_by("id").all()

    #1,重写数据源
    def get_queryset(self):
        #1,获取查询关键字
        keyword = self.request.query_params.get("keyword")

        #2,判断是否有关键字
        if keyword :
            return User.objects.filter(username__contains=keyword).order_by("id").all()
        else:
            return User.objects.order_by("id").all()


    # def post(self,request):
        # #1,获取参数
        # dict_data = request.data
        #
        # #2,获取序列化器,校验入库
        # serializer = self.get_serializer(data=dict_data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        #
        # #3,返回响应
        # return Response(status=201)

        #mixin配合
        # return self.create(request)
