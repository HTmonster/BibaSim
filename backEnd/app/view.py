'''
Author: Theo_hui
Date: 2020-10-15 18:15:53
Descripttion: 视图界面
'''
from flask import Flask, request, jsonify, g, Blueprint
from flask_httpauth import HTTPBasicAuth

from app.auth import auth
from app.models import User,Object,db

blue=Blueprint("biba",__name__)

# 注册蓝图
def init_blue(app):
    app.register_blueprint(blueprint=blue)

#---------------用户管理相关--------------------#
@blue.route('/api/token')
@auth.login_required
def get_auth_token():
    ''' 获得token '''
    token = g.user.generate_auth_token(600)
    return jsonify({"status":"OK","data":{'token': token.decode('ascii'), 'duration': 600}})


@blue.route("/api/login",methods=['POST'])
def user_login():
    ''' 用户认证 '''
    username    = request.json.get('username')
    password    = request.json.get('password')

    # 信息缺失
    if username is None or password is None:
        return jsonify({"status":"ERROR","msg":"parameter miss"})

    user = User.query.filter_by(username=username).first()
    # 无用户或者认证失败
    if not user or not user.verify_password(password):
        return jsonify({"status":"ERROR","msg":"verify fail"})
    #认证成功
    else:
        print(user.generate_auth_token(600))
        return jsonify({"status":"ok","token":user.generate_auth_token(600).decode('ascii')})
    
@blue.route('/api/users', methods=['GET','POST'])
@auth.login_required
def new_user():
    #新增一个用户
    if request.method=="POST":
        username    = request.json.get('username')
        password    = request.json.get('password')
        permission  = request.json.get("permission")
        if username is None or password is None:
            return jsonify({"status":"ERROR","msg":"parameter miss"})
        if User.query.filter_by(username=username).first() is not None:
            return jsonify({"status":"ERROR","msg":"user existed"})
        user = User(username=username,permission=permission)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"status":"OK",'username': user.username})
    #获得所有的用户
    elif request.method=="GET":
        #非超级用户
        if g.user.id!=1:
            return jsonify({"status":"ERROR","msg":"user isnot superuser"})
        users=User.query.with_entities(User.username,User.permission).all()
        return jsonify({"status":"OK","data":list(users)})
    else:
        return jsonify({"status":"ERROR","msg":"Unkown"})

#---------------资源管理相关--------------------#
@blue.route('/api/objects',methods=['GET'])
@auth.login_required
def get_objects():
    ''' 获得所有对象 '''
    S=g.user  #主体等级
    objects=Object.query.all() #获得所有客体资源

    data=[]
    for O in objects:
        writeable = True if S.permission>O.permission  else False
        readable  = True if S.permission<=O.permission else False
        data.append({'id':O.id,'name':O.name,'w':writeable,'r':readable})

    return jsonify({"status":"OK","data":data})

@blue.route('/api/objects/<int:id>',methods=['GET','POST'])
@auth.login_required
def get_object_content(id):
    ''' 获得一个对象的具体内容 '''
    o=Object.query.filter_by(id=id).first()
    if not o:
        return jsonify({"status":"ERROR","msg":"invalid id"})
    
    if request.method=="GET":
        return jsonify({"status":"OK","data":o.content})
    elif request.method=="POST":
        try:
            data    = request.json.get('data')
            o.content+=data
            db.session.commit()
            return jsonify({"status":"OK"})
        except:
            return jsonify({"status":"ERROR"})