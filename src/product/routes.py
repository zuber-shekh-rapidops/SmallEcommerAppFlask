# src/product/routes.py

# imports
from flask import Blueprint,render_template,redirect,url_for,flash,request,abort
from src.app import db,app
from src.product.models import ProductImagesModel,ProductModel
from src.product.forms import AddProductForm,AddProductImageForm,UpdateProductForm
from flask_login import current_user,login_required
from PIL import Image
import secrets
import os

# blueprint
product=Blueprint('product',__name__,url_prefix='/product')


def save_picture(image_file):
    '''function will save the picture into the local storage'''
    output_size=(200,200)
    random_hex=secrets.token_hex(8)
    i=Image.open(image_file)
    i.thumbnail(output_size)
    _,file_ext=os.path.splitext(image_file.filename)
    picture_file=random_hex+file_ext
    picture_path=os.path.join(app.root_path,'static/images/products',picture_file)
    i.save(picture_path)
    return picture_file


# localhost:5000/products/new
@product.route('/new',methods=['GET','POST'])
@login_required
def add_product():
    form=AddProductForm()
    if form.validate_on_submit():
        product=ProductModel(name=form.name.data,price=form.price.data,description=form.description.data,user_id=current_user.id)
        db.session.add(product)
        db.session.commit()
        flash('product added!')
        return redirect(url_for('user.home'))
    return render_template('product/new.html',form=form)

# localhost:5000/products/<id>
@product.route('/<int:id>')
@login_required
def view_product(id):
    product=ProductModel.query.get_or_404(id)
    if current_user.id!=product.user_id:
        abort(401)
    
    return render_template('product/show.html',product=product)
    

# localhost:5000/products/<id>/add/image
@product.route('/<int:id>/add/image',methods=['GET','POST'])
@login_required
def add_product_image(id):
    form=AddProductImageForm()
    if form.validate_on_submit():
        image=save_picture(form.image.data)
        pimage=ProductImagesModel(product_image=image,product_id=id)
        db.session.add(pimage)
        db.session.commit()
        flash("image saved")
        return redirect(url_for('product.view_product',id=id))

    return render_template('product/add_product_image.html',form=form)

# localhost:5000/products/<id>/update
@product.route('/<int:id>/update',methods=['GET','POST'])
@login_required
def update_product(id):
    uproduct=ProductModel.query.get_or_404(id)
    form=UpdateProductForm()
    if current_user.id!=uproduct.user.id:
        abort(401)
    if request.method=='GET':
        form.name.data=uproduct.name
        form.price.data=uproduct.price
        form.description.data=uproduct.description
    if form.validate_on_submit():
        uproduct.name=form.name.data
        uproduct.price=form.price.data
        uproduct.description=form.description.data
        db.session.commit()
        flash('product updated')
        return redirect(url_for('product.view_product',id=id))
    return render_template('product/update.html',form=form)

# localhost:5000/products/image/<id>/delete
@product.route('/image/<int:id>/delete')
@login_required
def delete_image(id):
    pimage=ProductImagesModel.query.get(id)
    db.session.delete(pimage)
    db.session.commit()
    flash('image deleted')
    return redirect(url_for('product.view_product',id=pimage.product_id))

# localhost:5000/products/<id>/delete
@product.route('/<int:id>/delete')
@login_required
def delete_product(id):
    dproduct=ProductModel.query.get_or_404(id)
    if current_user.id!=dproduct.user.id:
        abort()
    db.session.delete(dproduct)
    db.session.commit()
    flash('product deleted!')
    return redirect(url_for('user.home'))
