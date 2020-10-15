'''
Author: Theo_hui
Date: 2020-10-15 09:21:05
Descripttion: 配置文件
'''
import os	
basedir = os.path.abspath(os.path.dirname(__file__))	

class Config(object):	
    SQLALCHEMY_DATABASE_URI         ='sqlite:///' + os.path.join(basedir, 'app/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    SECRET_KEY = '*\xff\x93\xc8w\x13\x0e@3\xd6\x82\x0f\x84\x18\xe7\xd9\\|\x04e\xb9(\xfd\xc3'