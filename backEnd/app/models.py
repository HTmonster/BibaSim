'''
Author: Theo_hui
Date: 2020-10-15 18:11:04
Descripttion: 
'''
from flask_sqlalchemy import SQLAlchemy
import time
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = '*\xff\x93\xc8w\x13\x0e@3\xd6\x82\x0f\x84\x18\xe7\xd9\\|\x04e\xb9(\xfd\xc3'

#db对象
db = SQLAlchemy()

#----------------------用户------------------------------------#
class User(db.Model):
    __tablename__ = 'users'

    id              = db.Column(db.Integer, primary_key=True)  #id 主键
    username        = db.Column(db.String(32), index=True)     #用户名
    password_hash   = db.Column(db.String(128))                #密码 hash过的数据
    permission      = db.Column(db.Integer)                    #权限    

    # 密码hash
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)
    # 验证密码
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    # 产生Token
    def generate_auth_token(self, expires_in=600):
        return jwt.encode(
            {'id': self.id, 'exp': time.time() + expires_in},SECRET_KEY, algorithm='HS256')

    @staticmethod
    def verify_auth_token(token):
        try:
            data = jwt.decode(token, SECRET_KEY,algorithms=['HS256'])
        except:
            return
        return User.query.get(data['id'])

#----------------------对象------------------------------------#
class Object(db.Model):
    __tablename__ = 'object'

    id              = db.Column(db.Integer, primary_key=True)  #id 主键
    name            = db.Column(db.String(32), index=True)     #文件名字
    content         = db.Column(db.String(2048))               #文件的内容
    permission      = db.Column(db.Integer)    