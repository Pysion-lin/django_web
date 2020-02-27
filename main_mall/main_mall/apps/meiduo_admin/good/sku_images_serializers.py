from rest_framework import serializers
from goods.models import SKUImage,SKU

#1, sku image序列化器
class SKUImageViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKUImage
        fields = "__all__"

#2, sku序列化器
class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = ("id","name")