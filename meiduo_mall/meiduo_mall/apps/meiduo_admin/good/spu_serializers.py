from rest_framework import serializers
from goods.models import SPU,Brand,GoodsCategory

#1,spu信息序列化器
class SPUViewSetSerializer(serializers.ModelSerializer):

    #1,重写brand
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()

    #2,重写category
    category1 = serializers.StringRelatedField(read_only=True)
    category1_id = serializers.IntegerField()

    category2 = serializers.StringRelatedField(read_only=True)
    category2_id = serializers.IntegerField()

    category3 = serializers.StringRelatedField(read_only=True)
    category3_id = serializers.IntegerField()


    class Meta:
        model = SPU
        fields = "__all__"

#2,spu品牌信息
class SPUBrandSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

#3,spu分类信息
class SPUCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"