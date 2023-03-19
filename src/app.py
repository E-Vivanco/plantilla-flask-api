import os
from flask_cors import CORS
from flask import Flask,render_template,json, jsonify,request
#import mysql.connector
import requests
from flask_migrate import Migrate
from dotenv import load_dotenv
from models import db, User,Character


load_dotenv()

app = Flask(__name__)
app.url_map.slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] ="cualquier_palabra"
app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URI')
#CORS(app)

# rrl de starw urlSW
db.init_app(app)
Migrate(app,db) # db init, db migrate, db upgrade
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def home():
    return render_template('index.html')

# User routes
@app.route('/api/users', methods=['GET'])
def get_users():

    # SELECT * FROM users;
    users = User.query.all() 
    users = list(map(lambda user: user.serialize(), users))

    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def create_user():
    # INSERT INTO users() VALUES ()

    datos = request.get_json()
    user = User()
    user.name = datos['name']
    user.lastname = datos['lastname']
    user.email = datos['email']
    user.password = datos['password']
    user.save() # ejecuta add + commit


    return jsonify(user.serialize()), 201

@app.route('/api/users/<int:id>', methods=['PATCH'])
def update_user(id):
    # UPDATE user SET name="", lastname="" email="", password="" WHERE id = ?
    
    name = request.json.get('name') # None
    lastname = request.json.get('lastname') # None
    email =  request.json.get('email') # None
    password =  request.json.get('password') # None

    # SELECT * FROM users WHERE id = ?
    user = User.query.get(id)
    user.name = name
    user.lastname = lastname
    user.email = email
    user.password = password
    user.update()
    
    #db.session.commit()

    return jsonify(user.serialize()), 202

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    # SELECT * FROM users WHERE id = ?
    user = User.query.get(id)

    # DELETE FROM users WHERE id=?
    user.delete()

    return jsonify({ "message": "User Deleted" }), 202

@app.route('/api/characters', methods=['GET'])
def get_character():

    characters = Character.query.all()
    characters = list(map(lambda character: character.serialize(), characters))

    return jsonify(characters), 200

@app.route('/api/characters', methods=['POST'])
def create_character():

    datos = request.get_json()
    character = Character()
    character.name = datos['name']
    character.mass = datos['mass']
    character.skin = datos['skin']
    character.hair = datos['hair']
    character.save()

    return jsonify(character.serialize()), 201
@app.route('/api/characters/<int:id>', methods=['PATCH'])
def update_character(id):
    # UPDATE user SET name="" WHERE id = ?
    
    name = request.json.get('name') # None
    mass = request.json.get('mass') # None
    skin =  request.json.get('skin') # None
    hair =  request.json.get('hair') # None

    # SELECT * FROM users WHERE id #
    character = Character.query.get(id)
    character.name = name
    character.mass = mass
    character.skin = skin
    character.hair = hair
    character.update()
    
    
    return jsonify(character.serialize()), 202
    
@app.route('/api/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    # SELECT * FROM users WHERE id = ?
    character = Character.query.get(id)

    # DELETE FROM users WHERE id=?
    character.delete()

    return jsonify({ "message": "Character Deleted" }), 202





with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run()