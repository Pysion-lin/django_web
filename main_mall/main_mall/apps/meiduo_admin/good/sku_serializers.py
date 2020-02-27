from rest_framework import serializers
from goods.models import SKU,GoodsCategory,SPU,SPUSpecification,SpecificationOption,SKUSpecification
from django.db import transaction

#0,SKUSpecification序列化器
class SKUSpecificationSerializer(serializers.Serializer):
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

#1,sku序列化器
class SKUViewSetSerializer(serializers.ModelSerializer):

    #1,重写分类
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()

    #2,spu重写
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    #3,specs重写
    specs = SKUSpecificationSerializer(read_only=True,many=True)

    class Meta:
        model = SKU
        fields = "__all__"

    #3,重写create方法,保存sku和对应的规格
    @transaction.atomic
    def create(self, validated_data):

        #TODO 设置保存点
        sid = transaction.savepoint()

        try:
            #1,创建sku对象入库
            sku = SKU.objects.create(**validated_data)

            #2,创建规格信息入库
            specs = self.context["request"].data["specs"]
            for spec_dict in specs:
                SKUSpecification.objects.create(sku_id=sku.id,spec_id=spec_dict["spec_id"],option_id=spec_dict["option_id"])
        except Exception as e:
            transaction.savepoint_rollback(sid) #TODO 回滚
            raise serializers.ValidationError("保存失败")
        else:

            #3,返回响应,
            transaction.savepoint_commit(sid) #TODO 提交
            return sku

    #4,重写update方法,更新sku中的规格
    @transaction.atomic
    def update(self, instance, validated_data):

        #TODO 设置保存点
        sid = transaction.savepoint()

        try:
            #1,更新sku其他信息(标题,价格,...)
            SKU.objects.filter(id=instance.id).update(**validated_data)

            #1,1 删除以前所有的规格
            [spec.delete() for spec in instance.specs.all()]

            #2,更新规格信息入库
            specs = self.context["request"].data["specs"]
            for spec_dict in specs:
                SKUSpecification.objects.create(sku_id=instance.id,spec_id=spec_dict['spec_id'],option_id=spec_dict["option_id"])
        except Exception as e:
            transaction.savepoint_rollback(sid) #TODO 回滚
            raise serializers.ValidationError("保存失败")
        else:

            #3,返回响应,
            transaction.savepoint_commit(sid) #TODO 提交
            return SKU.objects.get(id=instance.id)

#2,sku商品分类序列化器
class SKUCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = ("id","name")

#3,sku简要信息序列化器
class SKUGoodSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPU
        fields = ("id","name")

# 商品规格的选项
class SpecificationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificationOption
        fields = ("id","value")


#4,sku的商品规格序列化器
class SKUGoodsSpecsSerializer(serializers.ModelSerializer):

    #1,重写spu
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    #2,重写option
    options = SpecificationOptionSerializer(read_only=True,many=True)

    class Meta:
        model = SPUSpecification
        fields = "__all__"