from rest_framework.views import APIView
from .serializers import BookInfoModelSerializer
from .models import BookInfo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework import mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action


# 1, 使用APIView和序列化器,实现列表视图(获取所有,创建单个)
class BookListAPIView(APIView):
    def get(self, request):
        # 1,获取所有书籍对象
        books = BookInfo.objects.all()

        # 2,创建序列化器
        serializer = BookInfoModelSerializer(instance=books, many=True)

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1,获取参数
        dict_data = request.data

        # 2,创建序列化器,校验,入库
        serializer = BookInfoModelSerializer(data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 2, APIView实现详情视图(获取单个,修改单个,删除单个)
class BookDetailAPIView(APIView):
    def get(self, request, pk):
        # 1,获取对象
        book = BookInfo.objects.get(pk=pk)

        # 2,创建序列化器
        serializer = BookInfoModelSerializer(instance=book)

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # 1,获取对象,数据
        book = BookInfo.objects.get(pk=pk)
        dict_data = request.data

        # 2,创建序列化器,校验,入库
        serializer = BookInfoModelSerializer(instance=book, data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # 1,获取参数
        book = BookInfo.objects.get(pk=pk)

        # 2,删除
        book.delete()

        # 3,返回
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3,二级视图: GenericAPIView,实现列表视图
"""
GenericAPIView特点:
1, GenericAPIView继承自APIView类，为标准列表和详细信息视图添加了常用的方法和属性。
    属性:
        serializer_class: 提供通用的序列化器
        queryset: 提供通用的数据源
        lookup_field: 默认值是pk,用来获取数据源中的单个数据的
        
    方法:
        get_serializer: 获取序列化器
        get_queryset: 获取数据源
        get_object:   根据pk获取单个对象,配合lookup_field
        

2, 该类可以和一个或多个mixin类组合而构建的。
作用: mixin类提供用于提供列表视图,详情视图,常见的行为操作(get,post,put,delete等等功能)
类名称                 提供的方法       作用
ListModelMixin          list           获取所有数据(get)
CreateModelMixin        create         创建单个对象(post)
RetrieveModelMixin      retrieve       获取单个对象(get)
UpdateModelMixin        update         修改单个对象(update)
DestroyModelMixin       destroy        删除单个对象(delete)

"""


class BookListGenericAPIView(GenericAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()

    def get(self, request):
        # 1,获取所有书籍对象
        # books = BookInfo.objects.all()
        books = self.get_queryset()

        # 2,创建序列化器
        # serializer = BookInfoModelSerializer(instance=books,many=True)
        # serializer = self.serializer_class(instance=books,many=True)
        # serializer = self.get_serializer_class(instance=books,many=True)
        # serializer = self.get_serializer_class(instance=books,many=True)
        serializer = self.get_serializer(instance=books, many=True)  # 和上面等价

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # 1,获取参数
        dict_data = request.data

        # 2,创建序列化器,校验,入库
        # serializer = BookInfoModelSerializer(data=dict_data)
        serializer = self.get_serializer(data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 3, 二级视图,GenericAPIView实现详情视图(获取单个,修改单个,删除单个)
class BookDetailGenericAPIView(GenericAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()

    # 3,重写lookup_field
    lookup_field = "id"

    def get(self, request, id):
        # 1,获取对象
        # book = BookInfo.objects.get(pk=pk)
        book = self.get_object()  # 根据pk在数据源中获取对应的对象

        # 2,创建序列化器
        serializer = self.get_serializer(instance=book)

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        # 1,获取对象,数据
        # book = BookInfo.objects.get(pk=pk)
        book = self.get_object()
        dict_data = request.data

        # 2,创建序列化器,校验,入库
        serializer = self.get_serializer(instance=book, data=dict_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3,返回响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        # 1,获取参数
        # book = BookInfo.objects.get(pk=pk)
        book = self.get_object()

        # 2,删除
        book.delete()

        # 3,返回
        return Response(status=status.HTTP_204_NO_CONTENT)


# 4,二级视图,GenericAPIView, MiXin配合使用,实现列表视图,详情视图功能
class BookListMiXinGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDetailMixinGenericAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                    GenericAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


# 5,三级视图
"""
特点: 已经提供好了对应的通用功能
类视图             父类                                方法          作用
CreateAPIView     GenericAPIView，CreateModelMixin    post         创建单个对象
ListAPIView       GenericAPIView，ListModelMixin      get          获取所有
RetrieveAPIView   GenericAPIView，RetrieveModelMixin  get          获取单个对象
DestroyAPIView    GenericAPIView，DestroyModelMixin   delete       删除单个对象
UpdateAPIView     GenericAPIView，UpdateModelMixin    put          修改单个对象
...

"""


# 6,三级视图,实现列表视图,详情视图功能
class BookListThreeView(ListAPIView, CreateAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()


class BookDetailThreeView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    # 1,提供通用的序列化器
    serializer_class = BookInfoModelSerializer

    # 2,提供通用的数据源
    queryset = BookInfo.objects.all()


# 7,视图集
"""
视图集名称                父类                         作用
ViewSet                 ViewSetMixin,APIView        可以进行路由映射
GenericViewSet          ViewSetMixin,GenericAPIView 可以进行路由映射,三个属性,三个方法
ModelViewSet            5个mixin, GenericViewSet     列表视图,详情视图, 三个属性,三个方法

ReadOnlyModelViewSet    ListModelmiXin,             获取单个,所有, 三个属性方法
                        RetrieveModelMixin,
                        GenericViewSet

"""
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from booktest.serializers import BookInfoModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving books.
    """

    def list(self, request):
        queryset = BookInfo.objects.all()
        serializer = BookInfoModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = BookInfo.objects.all()
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookInfoModelSerializer(book)
        return Response(serializer.data)


# 8,视图集ReadOnlyModelViewSet,实现获取功能
class BookReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()


# 9,使用ModelViewSet,实现列表,详情功能
class BookListDetailModelViewSet(ModelViewSet):
    serializer_class = BookInfoModelSerializer
    queryset = BookInfo.objects.all()

    # 1,获取阅读大于10,的书籍(额外动作)
    @action(methods=['get'], detail=False)  # 没有pk, 自动生成格式: 前缀/方法名/
    def haha(self, request):
        # 1,查询最大书籍
        books = BookInfo.objects.filter(bread__gte=30)

        # 2,创建序列化器对象
        serializer = self.get_serializer(instance=books, many=True)

        # 2,返回响应
        return Response(serializer.data)

    # 2,更新编号为1的书籍的阅读量
    @action(methods=['put'], detail=True)  # 有pk, 自动生成的格式: 前缀/{pk}/方法名
    def update_book(self, request, pk):
        # 1,获取书籍,数据
        book = self.get_object()
        dict_data = request.data

        # 2,获取序列化器对象,校验,入库
        serializer = self.get_serializer(instance=book, data=dict_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # 3,返回响应
        return Response(serializer.data)
