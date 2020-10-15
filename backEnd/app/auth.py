'''
Author: Theo_hui
Date: 2020-10-15 18:20:42
Descripttion: 用户认证
'''
from flask_httpauth import HTTPBasicAuth
from app.models import User
from flask import g

# 模块名称
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username_or_token, password):
    '''
    用户认证回调函数：  支持用户名+密码 和Token的认证方式
    '''    
    username_or_token.encode("ascii")
    #先尝试Token 认证
    print(User.verify_auth_token(username_or_token))
    user = User.verify_auth_token(username_or_token)
    if not user:
        # 再次尝试 用户+密码 认证
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
