# src/user/models.py
from src.app import db,bcrypt
from src.app import login_manager
from flask_login import UserMixin

# user loader
@login_manager.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

# ***********************************************************USER MODEL***********************************************************
class UserModel(db.Model,UserMixin):
    '''user model : representing user information in sql table'''

    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(256),nullable=False)
    mobile_no=db.Column(db.String(10),nullable=False)
    billing_address=db.Column(db.Text,nullable=True)
    delivery_address=db.Column(db.Text,nullable=True)
    products=db.relationship('ProductModel',backref='user',lazy=True,cascade='all,delete')

    def __init__(self,email,password,mobile_no):
        self.email=email
        self.password=bcrypt.generate_password_hash(password).decode('utf-8')
        self.mobile_no=mobile_no

    def update_password(self,password):
        '''update password'''
        self.password=bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return f"hello i am {self.email}"

    def check_password(self,password):
        '''check users password'''
        return bcrypt.check_password_hash(self.password,password)
