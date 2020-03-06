# src/product/models.py

# imports
from src.app import db

# ***********************************************************PRODUCT MODEL***********************************************************
class ProductModel(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    price=db.Column(db.Integer,nullable=False)
    description=db.Column(db.Text,nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    images=db.relationship('ProductImagesModel',backref='product',lazy=True,cascade="all,delete")
    
class ProductImagesModel(db.Model):
    __tablename__='productimages'
    id=db.Column(db.Integer,primary_key=True)
    product_image=db.Column(db.String,default='default_product.jpg')
    product_id=db.Column(db.Integer,db.ForeignKey('products.id'))