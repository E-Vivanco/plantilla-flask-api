from flask_cors import CORS
from flask import Flask,render_template,json, jsonify
#import mysql.connector
import requests
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db, User,Character,Planet,Vehicle,Favorito

load_dotenv()

app = Flask(__name__)
app.url_map.slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] ="cualquier_palabra"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///basedatosflask2.db"
#CORS(app)

# rrl de starw urlSW
db.init_app(app)
Migrate(app,db) # db init, db migrate, db upgrade
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    users= User.query.all()
    users=list(map(lambda user:user.serialize(),users))
    
    return jsonify({"Ok: ok",users}),200

    

    

if __name__ == '__main__':
    app.run()