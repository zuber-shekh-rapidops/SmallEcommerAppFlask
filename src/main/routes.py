# src/main/routes.py

# imports
from flask import render_template,Blueprint

# blueprint
main=Blueprint('main',__name__)

# localhost:5000/
@main.route('/')
def index():
    return render_template('main/index.html')

