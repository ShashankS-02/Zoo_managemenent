from flask import Flask
from apis import api
from model import db
from flask_cors import CORS
from flask import render_template

mysql_username = "root"
mysql_password = "Shandilya#2002"
mysql_host = "localhost"
mysql_port = "3306"
mysql_db = "ZMS"

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'
api.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()  # creates the table as configured in the database model

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# @app.route("/zms")
# def render():
    # return render_template("C:\Users\shash\Documents\PycharmProjects\Zoo_managemenent\templates\index.html")

db.init_app(app)
app.run(debug=True)