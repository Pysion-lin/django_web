from django.contrib.auth.backends import ModelBackend
import re
from users.models import User

#1,重写authenticate方法,认证用户
class MyModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):

        #0,通过request判断,是否是前端vue代码过来的
        if not request:
            #0.1查询用户名
            try:
                user = User.objects.get(username=username, is_superuser=True, is_staff=True)
            except Exception as e:
                return None

            #0.2 校验密码
            if user.check_password(password):
                return user

            return None


        #1,判断username是否是手机号的格式
        try:
            if re.match(r'^1[3-9]\d{9}$',username):
                user = User.objects.get(mobile=username)
            else:
                user = User.objects.get(username=username)
        except Exception:
            return None

        #2,校验密码
        if user.check_password(password):
            return user
        else:
            return None