# Books

-The Registration page is found in register.html
-The Login page is found in login.html
-Users are able to logout 
-Users are able to view their profile at account.html
-Importing of books.csv is done by import.py
-The Search page is found in search.html
-Users can search for books by ISBN number, title or author
-The Book page is found in book.html
-The layout is done by layout.html
-When users are logged in they can write a single review per book
-Users aren't able to write multiple reviews for a single book
-The GoodReads data is shown at the book page
-Users are able to access the API by browsing to /api/isbn
-The code for hashing the password is in the file fastpbkdf2-0.2
-The CSS is in styles.css


## Getting Started

This application is run with Flask
It consists of 3 postgresql databases: books, reviews and users

Table books:
id			integer Auto Increment
isbn		character varying
title 		character varying
author		character varying
year		integer

--------------------------

Table reviews:
book_id 	integer
user_id 	integer
comment		character varying
stars		integer

Foreign keys
book_id		books(id)
user_id 	users(id)

--------------------------

Table users:
id			integer Auto Increment
username	character varying
password	character varying
full_name 	character varying


Linking flask to the database:
Terminal => export DATABASE_URL="your postgresql database"


