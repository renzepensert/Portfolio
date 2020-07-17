import os

from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, fresh_login_required
from urllib.parse import urlparse, urljoin
from datetime import datetime

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

from models import *

# Configure Flask app
app = Flask(__name__)

# Configure database
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session, use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["USE_SESSION_FOR_NEXT"] = True
Session(app)

# Configure secret key
app.secret_key = os.environ['SECRET_KEY']

#app.config["SECRET_KEY"] = "2b18f1021903cff36d48a38ab2033801f12649d6df506584"

# Configure migrations
Migrate(app, db)

# Configure bootstrap
bootstrap = Bootstrap(app)


# Flask login, login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.refresh_view = "login"
login_manager.needs_refresh_message = "You need to re-login to access this page"

    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
    
# Makes sure only admins are able to view the admin page   
class MyModelView(ModelView):
    
    def is_accessible(self):
        
        user = User.query.filter_by(id=current_user.id).first()
        if user:
            if user.isadmin is True:
            
                return current_user.is_authenticated

# Admin page
admin = Admin(app, name='Pinocchio Admin', template_mode='bootstrap3')
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Rpizza, db.session))
admin.add_view(MyModelView(Spizza, db.session))
admin.add_view(MyModelView(Subs, db.session))
admin.add_view(MyModelView(Platters, db.session))
admin.add_view(MyModelView(Other, db.session))
admin.add_view(MyModelView(Toppings, db.session))
admin.add_view(MyModelView(Extras, db.session))
admin.add_view(MyModelView(Cart, db.session))
admin.add_view(MyModelView(Order, db.session))
    

# Index    
@app.route("/")
def index():
    return render_template("index.html")

# Login    
@app.route("/login", methods=["GET", "POST"])
def login():
    
    #Checks if username is in database
    user = User.query.filter_by(username=request.form.get("username")).first()
    if user:
        #Checks password
        if check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for("index"))
        
    return render_template("login.html")
    

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("http", "https") and \
           ref_url.netloc == test_url.netloc
    

# Checks if username already exists 
@app.route("/checkuser", methods=["POST"])
def checkuser():
    # Make a list of all usernames
    usernames = []
    users = User.query.all()
    for user in users:
        usernames.append(user.username)
    
    # Get the username from the register form
    username=request.form.get("username")
   
    # Checks if username is already in the database
    if username in usernames:
        return jsonify({"success": False})
       
    return jsonify({"success": True})
    


@app.route("/signup", methods=["GET", "POST"])
def signup():
    # Checks if username is already in database
    user_check = User.query.filter_by(username=request.form.get("username")).first()
    
    if request.method == "POST":
        if user_check:
            # Username is already in the database
            return render_template("signup.html")
            
        else:
            #Create new account    
            hashed_password = generate_password_hash(request.form.get("password"), method='sha256')
            
            new_user = User(username=request.form.get("username"), email=request.form.get("email"), 
            password=hashed_password, firstname=request.form.get("firstname"), 
            lastname=request.form.get("firstname"), isadmin=False)
            
            # Add user and commit to database
            db.session.add(new_user)
            db.session.commit()
                
            return redirect(url_for("login"))
    
    return render_template("signup.html")
    

# Add items from the menu to the shopping cart
@app.route("/addtocart", methods=["POST"])
@login_required
def addtocart():
    
    # Count the amount of toppings selected
    topping_amount = 0
    if request.form.get("toppings1") != "None":
        topping_amount = topping_amount + 1
    if request.form.get("toppings2") != "None":
        topping_amount = topping_amount + 1
    if request.form.get("toppings3") != "None":
        topping_amount = topping_amount + 1
    if request.form.get("toppings4") != "None":
        topping_amount = topping_amount + 1
        
    
    # Load all the databases    
    regular = Rpizza.query.all()
    sicilian = Spizza.query.all()
    subs = Subs.query.all()
    platters = Platters.query.all()
    other = Other.query.all()
    toppings = Toppings.query.all()
    extras = Extras.query.all()
    
    if request.form.get("radio") == "small":
        size = 1
    else: 
        size = 2
    
    # Handles regular pizza orders from menu
    if request.form.get("order").startswith('regular'):
        pizzaname = ''.join(request.form.get("order").split('regular ',1))
        pizza = Rpizza.query.filter_by(name=pizzaname)
           
        if pizza:
            if size == 1:
                if topping_amount == 0:
                    price = pizza[0].price
                if topping_amount == 1:
                    price = pizza[0].price3
                if topping_amount == 2:
                    price = pizza[0].price5
                if topping_amount == 3:
                    price = pizza[0].price7
                if topping_amount == 4:
                    price = pizza[0].price9
            if size == 2:
                if topping_amount == 0:
                    price = pizza[0].price1
                if topping_amount == 1:
                    price = pizza[0].price4
                if topping_amount == 2:
                    price = pizza[0].price6
                if topping_amount == 3:
                    price = pizza[0].price8
                if topping_amount == 4:
                    price = pizza[0].price10
            
            
        
        new_order = Cart(userid=current_user.id, username=current_user.username, 
        order=request.form.get("order") + " " + request.form.get("radio") + " " + request.form.get("toppings1")
         + " " + request.form.get("toppings2") + " " + request.form.get("toppings3") + " " + request.form.get("toppings4"), total=price)
        db.session.add(new_order)
        db.session.commit()
    
    # Handles sicilian pizza orders from menu        
    if request.form.get("order").startswith('sicilian'):
        pizzaname = ''.join(request.form.get("order").split('sicilian ',1))
        pizza = Spizza.query.filter_by(name=pizzaname)
        
        if pizza:
            if size == 1:
                if topping_amount == 0:
                    price = pizza[0].price
                if topping_amount == 1:
                    price = pizza[0].price3
                if topping_amount == 2:
                    price = pizza[0].price5
                if topping_amount == 3:
                    price = pizza[0].price7
                if topping_amount == 4:
                    price = pizza[0].price9
            if size == 2:
                if topping_amount == 0:
                    price = pizza[0].price1
                if topping_amount == 1:
                    price = pizza[0].price4
                if topping_amount == 2:
                    price = pizza[0].price6
                if topping_amount == 3:
                    price = pizza[0].price8
                if topping_amount == 4:
                    price = pizza[0].price10
        
        
        new_order = Cart(userid=current_user.id, username=current_user.username, 
        order=request.form.get("order") + " " + request.form.get("radio") + " " + request.form.get("toppings1")
         + " " + request.form.get("toppings2") + " " + request.form.get("toppings3") + " " + request.form.get("toppings4"), total=float(price))
        db.session.add(new_order)
        db.session.commit()
    
    # Handles sub orders from menu
    if request.form.get("order").startswith('sub'):
        subname = ''.join(request.form.get("order").split('sub ',1))      
        sub = Subs.query.filter_by(name=subname)
        if sub:
            if size == 1:
                price = sub[0].price
            if size == 2:
                price = sub[0].price2
        extra=[]
        
        
        for items in extras:
            
            if request.form.get(items.name):
                cheese = Extras.query.filter_by(name=items.name)
            
            
                price100 = cheese[0].price
                price = price + price100
                extra.append(items.name)
            
            
        new_order = Cart(userid=current_user.id, username=current_user.username, order=request.form.get("order") + " " + request.form.get("radio") + " " + str(extra), total=price)
        
        db.session.add(new_order)
        db.session.commit()
    
    # Handles platter orders from menu
    if request.form.get("order").startswith('platter'):
        plattername = ''.join(request.form.get("order").split('platter ',1))
        platter = Platters.query.filter_by(name=plattername)
        if platter:
            if size == 1:
                price = platter[0].price
            if size == 2:
                price = platter[0].price2
                
        new_order = Cart(userid=current_user.id, username=current_user.username, order=request.form.get("order") + " " + request.form.get("radio"), total=price)
        
        db.session.add(new_order)
        db.session.commit()
        
    # Handles pasta orders from menu
    if request.form.get("order").startswith('pasta'):
        pastaname = ''.join(request.form.get("order").split('pasta ',1))
        pasta = Other.query.filter_by(name=pastaname)
        if pasta:
            price = pasta[0].price
        
        new_order = Cart(userid=current_user.id, username=current_user.username, order=request.form.get("order"), 
        total=float(price))
        
        db.session.add(new_order)
        db.session.commit()
    
    # Sets anchors
    if request.form.get("order").startswith('pasta'):
        anchor = "pasta"
    elif request.form.get("order").startswith('platter'):
        anchor = "platter"
    else:
        anchor = "menu"
    
           
    return redirect(url_for('pizza', _anchor=anchor))


# Log Out the user
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
    
   
# Shopping Cart
@app.route("/cart")
@login_required
def cart():
    
    subtotal = 0
    order = Cart.query.filter_by(username=current_user.username)
    
    return render_template("cart.html", name=current_user, order=order)
    
# Menu pizzas and subs
@app.route("/pizza")
@login_required
def pizza():
    
    
    regular = Rpizza.query.all()
    sicilian = Spizza.query.all()
    subs = Subs.query.all()
    platters = Platters.query.all()
    other = Other.query.all()
    toppings = Toppings.query.all()
    extras = Extras.query.all()
       
    return render_template("pizza.html", regular=regular, sicilian=sicilian, subs=subs, platters=platters, other=other,
    toppings=toppings, extras=extras)
    
# Empty Shopping Cart
@app.route("/emptycart", methods=["POST"])
@login_required
def emptycart():
    cart = Cart.query.filter_by(userid=current_user.id).all()
    for cartlist in cart:
        empty = Cart.query.filter_by(userid=current_user.id).first()
        if empty:
            db.session.delete(empty)
            db.session.commit()
    
    return redirect(url_for('cart'))


# Pay the order, move from cart to order database and empty the cart
@app.route("/payout", methods=["POST"])
@login_required
def payout():
    paid = True
    cart = Cart.query.filter_by(userid=current_user.id).all()
    
    # Take the highest ordernumber and increment it by 1
    ordernumber = Order.query.order_by(-Order.ordernumber).first()
    ordernumber = ordernumber.ordernumber + 1
    
    for cartlist in cart:
        # Removes the order from cart
        payout = Cart.query.filter_by(userid=current_user.id).first()
        db.session.delete(payout)
        
        # Adds order from cart to Order database
        pay = Order(userid=current_user.id, username=current_user.username, order=payout.order, total=payout.total, 
        date=datetime.now(), paid=paid, ordernumber=ordernumber)
        
        db.session.add(pay)
        db.session.commit()
              
              
    return redirect(url_for('cart'))

# Runs application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
