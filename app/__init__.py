from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app=app)

migrate = Migrate(app=app,db=db)

login_manager = LoginManager(app=app)



from app import views, authentication, models
