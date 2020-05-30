from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime

db = SQLAlchemy()

# Maak een tabel aan voor users
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    isadmin = db.Column(db.Boolean)
    
# database Regular Pizza
class Rpizza(UserMixin, db.Model):
    __tablename__ = 'rpizza'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))
    price2 = db.Column(db.DECIMAL(2, 2))
    price3 = db.Column(db.DECIMAL(2, 2))
    price4 = db.Column(db.DECIMAL(2, 2))
    price5 = db.Column(db.DECIMAL(2, 2))
    price6 = db.Column(db.DECIMAL(2, 2))
    price7 = db.Column(db.DECIMAL(2, 2))
    price8 = db.Column(db.DECIMAL(2, 2))
    price9 = db.Column(db.DECIMAL(2, 2))
    price10 = db.Column(db.DECIMAL(2, 2))
    
    
# database Sicilian Pizza    
class Spizza(UserMixin, db.Model):
    __tablename__ = 'spizza'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))
    price2 = db.Column(db.DECIMAL(2, 2))
    price3 = db.Column(db.DECIMAL(2, 2))
    price4 = db.Column(db.DECIMAL(2, 2))
    price5 = db.Column(db.DECIMAL(2, 2))
    price6 = db.Column(db.DECIMAL(2, 2))
    price7 = db.Column(db.DECIMAL(2, 2))
    price8 = db.Column(db.DECIMAL(2, 2))
    price9 = db.Column(db.DECIMAL(2, 2))
    price10 = db.Column(db.DECIMAL(2, 2))
    
    
class Extras(UserMixin, db.Model):
    __tablename__ = 'extras'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))

# Database Subs
class Subs(UserMixin, db.Model):
    __tablename__ = 'subs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))
    price2 = db.Column(db.DECIMAL(2, 2))
    
# Database Toppings
class Toppings(UserMixin, db.Model):
    __tablename__ = 'toppings'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))

# Database Dinner Platters    
class Platters(UserMixin, db.Model):
    __tablename__ = 'platters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))
    price2 = db.Column(db.DECIMAL(2, 2))
    
# Database Pasta and Salads
class Other(UserMixin, db.Model):
    __tablename__ = 'other'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    price = db.Column(db.DECIMAL(2, 2))

# Database Shopping Cart    
class Cart(UserMixin, db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer())
    username = db.Column(db.String())
    order = db.Column(db.String())
    total = db.Column(db.DECIMAL(2, 2))
    
# Database Order
class Order(UserMixin, db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer())
    username = db.Column(db.String())
    order = db.Column(db.String())
    total = db.Column(db.DECIMAL(2, 2))
    ordernumber = db.Column(db.Integer())
    date = db.Column(db.DateTime())
    paid = db.Column(db.Boolean())