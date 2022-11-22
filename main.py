from flask import Flask
from apis import api
from model import db

mysql_username = "root"
mysql_password = "Shandilya#2002"
mysql_host = "localhost"
mysql_port = "3306"
mysql_db = "ZMS"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'
api.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()  # creates the table as configured in the database model


db.init_app(app)
app.run(debug=True)