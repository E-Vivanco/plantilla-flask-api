from flask import Flask,render_template
import mysql.connector
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.url_map.slashes=False
app.config['DEBUG']=True
app.config['ENV']='development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///basedatosflask2.db"


db.init_app(app)
Migrate(app,db) # db init, db migrate, db upgrade

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()