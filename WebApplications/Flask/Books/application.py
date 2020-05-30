import os
import time
import requests

from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from passlib.hash import pbkdf2_sha256
from datetime import date
from datetime import datetime 

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# todo set up goodreads
goodreads_key = '2nCqWHuNign7GPATQjIchQ'

book1 = "global"


# index
@app.route("/")
def index():
    
    # keep track if user is logged in
    try:
        id = session["user_id"]
    # gives a message when user is not logged in
    except:
        return render_template("index.html", info_msg="You are not logged in yet. Please log in before you can write a review.")
    return render_template("index.html")


# login
@app.route("/login", methods=["GET", "POST"])
def login():
    
    # clears all keys and values from the session-state collection
    session.clear()
    
    if request.method == "POST":
        # checks if user entered a username
        if not request.form.get("username"):
            return render_template("login.html", danger_msg="Please enter your username.")
        # checks if user entered a password
        elif not request.form.get("password"):
            return render_template("login.html", danger_msg="Please enter your password.")
        else:
            username = request.form.get("username")
            user = db.execute("SELECT * FROM users WHERE username=:username;", {"username": username}).fetchone()
            if user is not None:
                password = request.form.get("password")
                passwd = user['password']
                
                # use the verify method to check if password is correct
                if pbkdf2_sha256.verify(password, passwd):
                    session["user_id"] = user["id"]
                    session["name"] = user["full_name"].split(" ")[0]
                    return render_template("index.html", succes_msg="you were succesfully logged in.")
                else:
                    return render_template("login.html", danger_msg="Incorrect password.")
            else:
                return render_template("login.html", danger_msg="User does not exist.")
    else:
        return render_template("login.html")
        
# Register user
@app.route("/register", methods=["GET", "POST"])
def register():
    
    # clears all keys and values from the session-state collection
    session.clear()
    
    # checks if user has filled in every element in the form
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("register.html", danger_msg="Please enter your username.")
        elif not request.form.get("fullname"):
            return render_template("register.html", danger_msg="Please enter your full name.")
        elif not request.form.get("password"):
            return render_template("register.html", danger_msg="Please enter your password.")
        elif not request.form.get("confirm"):
            return render_template("register.html", danger_msg="Please repeat your password.")
        # password and confirm must be the same
        elif request.form.get("password") != request.form.get("confirm"):
            return render_template("register.html", danger_msg="Passwords do not match.")
        # password must be 4 characters or longer for security reasons
        elif len(request.form.get("password")) < 4:
            return render_template("register.html", danger_msg="Password must be at least 4 characters long.")
        # checks if username is already taken
        else:
            username = request.form.get("username")
            user = db.execute("SELECT * FROM users WHERE username=:username;", {"username": username}).fetchone()
            # create the user when username is not already taken
            if user is None:
                fullname = request.form.get("fullname")
                password = request.form.get("password")
                db.execute("INSERT INTO users (username, full_name, password) VALUES (:username, :fullname, :hash);", {"username": username, "fullname": fullname, "hash": pbkdf2_sha256.hash(password)})
                db.commit()
                return render_template("login.html", succes_msg="User succesfully created. Please log in now.")
            else:
                return render_template("register.html", danger_msg="User already exists.")
    else:
        return render_template("register.html")
        
# Log out
@app.route("/logout")
def logout():
    
    # clears all keys and values from the session-state collection
    session.clear()
    return render_template("login.html", succes_msg="You were succesfully logged out.")

# search books
@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        if request.form.get("search"):
            search = request.form.get("search").lower()
        if request.args.get("search"):
            search = request.args.get("search").lower()
        search1 = "%" + search + "%"
        books = db.execute("SELECT * FROM books WHERE lower(title) LIKE :search OR lower(author) LIKE :search OR lower(isbn) LIKE :search", {"search": search1}).fetchall()
        return render_template("search.html", books=books)
        
# account page
@app.route("/account", methods=["GET"])
def account():
    user = db.execute("SELECT * FROM users WHERE id = :user_id", {"user_id": session["user_id"]}).fetchone()
    return render_template("account.html", user=user)
    
# book page
@app.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "POST":
        id = request.args.get("id")
        book = db.execute("SELECT * FROM books WHERE id = :id", {"id": id}).fetchall()
        isbn = book[0]['isbn']
        global book1
        book1 = book[0]
        res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": goodreads_key, "isbns": isbn})
        book_id = book[0]['id']
        reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id ", {"book_id": book_id}).fetchall()
        names = []
        for review in reviews:
            userid = review['user_id']
            username = db.execute("SELECT * FROM users WHERE id = :id ", {"id":userid}).fetchone()['username']
            names.append(username)
            print(reviews)
        return render_template("book.html", book=book[0], review=res.json()['books'][0], reviews=reviews, names=names)
        
# search for or write a review
@app.route("/review", methods=["GET", "POST"])
def review():
    if request.method == "POST":
        global book1
        bookid = book1['id']
        try:
            user_id = session["user_id"]
            comment = request.form.get("comment")
            stars = int(request.form.get("stars"))
            res= requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": goodreads_key, "isbns": book1['isbn']})
            reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id ", {"book_id": bookid}).fetchall()
            names = []
            for review in reviews:
                userid = review['user_id']
                username = db.execute("SELECT * FROM users WHERE id = :id ", {"id": userid}).fetchone()['username']
                names.append(username)
            # checks if user has not already made a review about the book
            reviews1 = db.execute("SELECT * FROM reviews WHERE user_id=:user_id AND book_id=:book_id;", {"user_id": user_id, "book_id": bookid}).fetchone()
            if reviews1 is None:
                # insert the review into the database
                db.execute("INSERT INTO reviews (book_id, user_id, comment, stars) VALUES (:book_id, :user_id, :comment, :stars);", {"book_id": bookid, "user_id": user_id, "comment": comment, "stars": stars})
                db.commit()
                
                reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id ", {"book_id": bookid}).fetchall()
                names = []
                for review in reviews:
                    userid = review['user_id']
                    username = db.execute("SELECT * FROM users where id = :id ", {"id": userid}).fetchone()['username']
                    names.append(username)
                return render_template("book.html", book=book1, review=res.json()['books'][0], reviews = reviews, names=names, succes_msg="You have succesfully written a review for this book.")
            else:
                return render_template("book.html", book=book1, review=res.json()['books'][0], reviews = reviews, names =names, danger_msg="You have already written a review for this book.")
        except KeyError:
            res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": goodreads_key, "isbns": book1['isbn']})
            reviews = db.execute("SELECT * FROM reviews WHERE book_id = :book_id ", {"book_id": bookid}).fetchall()
            names = []
            for review in reviews:
                userid = review['user_id']
                username = db.execute("SELECT * FROM users WHERE id = :id ", {"id: userid"}).fetchone()['username']
                names.append(username)
            return render_template("book.html", book=book1, review=res.json()['books'][0], reviews=reviews, names=names, danger_msg="ERROR! You are not logged in.")
            
# Return information about the book when API is given
@app.route("/api/<path>", methods=["GET", "POST"])
def api(path):
    book1 = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": path}).fetchone()
    # checks if there is a book with isbn which patches the path
    if book1 is None:
        abort(404)
    book = list(book1)
    try:
        avg = db.execute("SELECT AVG(stars) FROM reviews WHERE book_id = :id", {"id": book[0]}).fetchone()[0]
    except:
        avg = 0
    try:
        rev = db.execute("SELECT COUNT(comment) FROM reviews WHERE book_id = :id", {"id": book[0]}).fetchone()[0]
    except:
        rev = 0
    book.append(path)
    book.append(rev)
    try:
        book.append(round(float(avg),2))
    except:
        book.append(0)
    list1 = ['title', 'author', 'year', 'isbn', 'review_count', 'average_score']
    book.pop(0)
    book.pop(0)
    ans = dict(zip(list1,book))
    return ans