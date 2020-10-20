'''
Author: Theo_hui
Date: 2020-10-15 09:29:20
Descripttion: 
'''
from flask import Flask
from flask_cors import CORS

from app.models import db
from app.view   import init_blue
from config import Config

if __name__ == '__main__':
    app = Flask(__name__)	
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    init_blue(app)
    
    print(app.url_map)
    app.run(debug=True)