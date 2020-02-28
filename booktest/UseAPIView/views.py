from rest_framework.views import APIView
from .serializers import BookInfoModelSerializer
from .models import BookInfo
from rest_framework.response import Response
from rest_framework import status

#1, 使用APIView和序列化器,实现列表视图(获取所有,创建单个)
class BookListAPIView(APIView):
    def get(self,request):
        #1,获取所有书籍对象
        books = BookInfo.objects.all()

        #2,创建序列化器
        serializer = BookInfoModelSerializer(instance=books,many=True)

        #3,返回响应
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        #1,获取参数
        dict_data = request.data

        #2,创建序列化器,校验,入库
        serializer = BookInfoModelSerializer(data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #3,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

#2, APIView实现详情视图(获取单个,修改单个,删除单个)
class BookDetailAPIView(APIView):
    def get(self,request,pk):
        #1,获取对象
        book = BookInfo.objects.get(pk=pk)

        #2,创建序列化器
        serializer = BookInfoModelSerializer(instance=book)

        #3,返回响应
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        #1,获取对象,数据
        book = BookInfo.objects.get(pk=pk)
        dict_data = request.data

        #2,创建序列化器,校验,入库
        serializer = BookInfoModelSerializer(instance=book,data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #3,返回响应
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        #1,获取参数
        book = BookInfo.objects.get(pk=pk)

        #2,删除
        book.delete()

        #3,返回
        return Response(status=status.HTTP_204_NO_CONTENT)