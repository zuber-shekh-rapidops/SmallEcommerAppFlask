# src/error/routes.py

# imports
from flask import Blueprint,redirect,render_template

error=Blueprint('error',__name__,'/error')

# localhost:5000/error/404
@error.app_errorhandler(404)
def error_404(error):
    return render_template('error/404.html'),404

# localhost:5000/error/401
@error.app_errorhandler(401)
def error_401(error):
    return render_template('error/401.html'),401

# localhost:5000/error/400
@error.app_errorhandler(400)
def error_400(error):
    return render_template('error/400.html'),400