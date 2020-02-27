from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from users.models import User
from datetime import date,timedelta
from rest_framework.generics import GenericAPIView
from goods.models import GoodCategoryVisit
from . import serializers

#1,获取用户总数
class UserTotalCountView(APIView):
    def get(self,request):
        #1,查询用户总数
        # count = User.objects.filter(is_superuser=False,is_staff=False).count()
        count = User.objects.count()

        #2,返回响应
        return Response({
            "count":count
        })

#2,获取用户日增数
class UserIncrementCountView(APIView):
    def get(self,request):
        #1,查询用户日增数
        today = date.today()
        count = User.objects.filter(date_joined__gte=today).count()

        #2,返回响应
        return Response({
            "count":count
        })

#3,获取日活数
class UserDayActiveCountView(APIView):
    def get(self, request):
        # 1,查询用户日活数
        today = date.today()
        count = User.objects.filter(last_login__gte=today).count()

        # 2,返回响应
        return Response({
            "count": count
        })

#4,获取日下单用户
class UserDayOrderCountView(APIView):
    def get(self, request):
        # 1,查询用户日下单数
        today = date.today()
        count = User.objects.filter(orderinfo__create_time__gte=today).count()

        # 2,返回响应
        return Response({
            "count": count
        })

#5,获取月增用户
class UserMonthIncreamentCountView(APIView):
    def get(self,request):

        #1,获取当天日期
        today = date.today()

        #2,获取30天前的日期
        old_date = today - timedelta(days=29)

        #3,循环查出每天的新增数,添加列表
        users_list = []
        for i in range(0,30):

            #3,1 获取当天时间
            current_date = old_date + timedelta(days=i)

            #3,2 获取当天时间的下一天
            next_date = old_date + timedelta(days=i+1)

            #3,3 查询新增数
            count = User.objects.filter(date_joined__gte=current_date,date_joined__lt=next_date).count()

            #3,4 添加数据
            users_list.append({
                "date":current_date,
                "count":count
            })

        #4,返回响应
        return Response(users_list)

#6,商品分类访问量
class UserGoodsVisitCountView(GenericAPIView):
    serializer_class = serializers.UserGoodsVisitCountSerializer

    def get(self,request):
        #1,获取当天时间
        today = date.today()
        goods_visit_count = GoodCategoryVisit.objects.filter(date__gte=today).all()

        #2,获取序列化器
        serializer = self.get_serializer(instance=goods_visit_count,many=True)

        #3,返回响应
        return Response(serializer.data)