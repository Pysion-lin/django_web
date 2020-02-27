from rest_framework import serializers
from goods.models import SpecificationOption,SPUSpecification

#1, spec option 序列化器
class SpecOptionsViewSetSerializer(serializers.ModelSerializer):

    #1,重写spec
    spec = serializers.StringRelatedField(read_only=True)
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = "__all__"

#2, spec 序列化器
class OptionSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = SPUSpecification
        fields = ("id","name")