from rest_framework import serializers
from orders.models import OrderInfo,OrderGoods
from goods.models import SKU

#1,orderinfo序列化器
class OrderViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        fields = "__all__"

#2,order ordergoods, sku序列化器
class SKUModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ("name","default_image_url")

class OrderGoodsModelSerializer(serializers.ModelSerializer):

    #1,重写sku
    sku = SKUModelSerializer(read_only=True)

    class Meta:
        model = OrderGoods
        fields = ("sku","price","count")

class OrdersModelSerializer(serializers.ModelSerializer):

    #1,重写skus,实际就是Ordergoods
    skus = OrderGoodsModelSerializer(read_only=True,many=True)

    class Meta:
        model = OrderInfo
        # fields = ("order_id","status","create_time",
        #           "user","total_count","total_amount",
        #           "freight","pay_method","skus")
        fields = "__all__"