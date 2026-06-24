from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()


class User(db.Model): 
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    public_id=db.Column(db.String(30),unique=True,nullable=False) 
    name=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),unique=True,nullable=False)
    password=db.Column(db.String(),nullable=False)
    
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(),nullable=False)
    products=db.relationship("Product",backref="Category",lazy=True,cascade='all,delete-orphan')
    
    
class Product(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(),nullable=False)
    price=db.Column(db.Float(),nullable=False)
    category_id=db.Column(db.Integer,db.ForeignKey("category.id"),nullable=False)
    



    
    