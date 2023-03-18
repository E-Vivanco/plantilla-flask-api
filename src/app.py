from flask import Flask,render_template,json, jsonify
import mysql.connector
import requests
from flask_migrate import Migrate
from models import db
app = Flask(__name__)
app.url_map.slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///basedatosflask2.db"

# rrl de starw urlSW
db.init_app(app)
Migrate(app,db) # db init, db migrate, db upgrade

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/get_users', methods=['GET'])
def get_users():
    usrlSW='https://www.swapi.tech/api/people'
    data= requests.get(usrlSW)
    peoples= lista_peoples()
    if data.status_code == 200:
        data = data.json()
    for pep in data["results"]:
        people=Peoples()
        print(pep)
        people.name= pep['name']
        people.uid=pep['uid']
        people.url=pep['url']
        people.save()

        return jsonify({"consulta ok"}), 200

    

if __name__ == '__main__':
    app.run()