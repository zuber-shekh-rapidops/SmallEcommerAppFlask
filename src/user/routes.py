# src/user/routes.py

# imports
from flask import Blueprint,render_template,redirect,flash,request,url_for,abort
from src.app import db
from src.user.forms import LoginForm,SignupForm,UpdateUserForm,UpdatePasswordForm
from src.user.models import UserModel
from flask_login import login_user,logout_user,login_required,current_user

# blueprint
user=Blueprint('user',__name__,url_prefix='/user')

# routes
# localhost:5000/user/login
@user.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))
    form=LoginForm()
    if form.validate_on_submit():
        user=UserModel.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('login successfully!')    

        return redirect(url_for('user.login'))
    return render_template('user/login.html',form=form)

# localhost:5000/user/signup
@user.route('/signup',methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('user.home'))
    form=SignupForm()
    if form.validate_on_submit():
        user=UserModel(email=form.email.data,password=form.password.data,mobile_no=form.mobile.data)
        db.session.add(user)
        db.session.commit()
        flash('user created successfully!')
        return redirect(url_for('user.login'))
    return render_template('user/signup.html',form=form)

# localhost:5000/user/home
@user.route('/home')
@login_required
def home():
    return render_template('user/home.html')

# localhost:5000/user/account
@user.route('/account')
@login_required
def account():
    return render_template('user/account.html')

# localhost:5000/user/<id>update
@user.route('/<int:id>/update',methods=['GET','POST'])
@login_required
def update_user(id):
    form=UpdateUserForm()
    uuser=UserModel.query.get(id)
    if current_user.id!=uuser.id:
        abort(401)
    if request.method=='GET':
        form.email.data=uuser.email
        form.mobile.data=uuser.mobile_no
        form.baddress.data=uuser.billing_address
        form.daddress.data=uuser.delivery_address
    if form.validate_on_submit():
        uuser.email=form.email.data
        uuser.mobile_no=form.mobile.data
        uuser.billing_address=form.baddress.data
        uuser.delivery_address=form.daddress.data
        db.session.commit()
        flash('user information updated!')
        return redirect(url_for('user.account'))
    return render_template('user/update.html',form=form)

# localhost:5000/user/products
@user.route('/products')
@login_required
def view_all_products():
    return render_template('user/view_products.html')

# localhost:5000/user/update_password
@user.route('/update/password/<int:id>',methods=['GET','POST'])
@login_required
def update_password(id):
    form=UpdatePasswordForm()
    uuser=UserModel.query.get_or_404(id)
    if current_user.id!=uuser.id:
        abort(401)
    if form.validate_on_submit():
        if uuser.check_password(form.opassword.data):
            uuser.update_password(form.password.data)
            db.session.commit()
            flash('user password updated')
            return redirect(url_for('user.account'))
        else:
            flash("please enter valid old password")
            return redirect(url_for('user.update_password',id=current_user.id))
    return render_template('user/update_password.html',form=form)

# localhost:5000/user/logout
@user.route('/logout')
@login_required
def logout():
    logout_user()
    flash('logout successfully!')
    return redirect(url_for('user.login'))

