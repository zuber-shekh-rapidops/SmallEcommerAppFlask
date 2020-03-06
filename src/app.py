# src/app.py

# imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# configurations
BASEDIR=os.path.abspath(os.path.dirname(__name__))
app=Flask(__name__)
app.config['SECRET_KEY']='secret_key'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(BASEDIR,'myecommerce.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)
Migrate(app,db)
login_manager=LoginManager(app)
bcrypt=Bcrypt(app)

# blueprints import
from src.main.routes import main
from src.user.routes import user
from src.product.routes import product
from src.error.routes import error

# blueprint registration
app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(error)

# routes imports
from src.main import routes
from src.user import routes
from src.product import routes
from src.error import routes