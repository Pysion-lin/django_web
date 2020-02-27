from rest_framework import serializers
from goods.models import GoodCategoryVisit

#1,商品分类访问量,序列化器
class UserGoodsVisitCountSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GoodCategoryVisit
        fields = "__all__"