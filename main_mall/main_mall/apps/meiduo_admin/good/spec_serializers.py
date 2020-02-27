from rest_framework import serializers
from goods.models import SPUSpecification

#1,spec序列化器
class SpecViewSetSerializer(serializers.ModelSerializer):

    #1,spu重写
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = "__all__"