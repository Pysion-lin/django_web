from rest_framework import serializers
from users.models import User

#1,用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","mobile","email","password")

        #添加额外的约束, write_only,只写
        extra_kwargs = {
            "password":{
                "write_only":True
            }
        }

    #1,重写create方法,密码加密处理
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)