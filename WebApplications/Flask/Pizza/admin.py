from models import *
from werkzeug.security import generate_password_hash
'''
Admin.py
Used to create admin accounts manually
How to use:
Terminal => flask shell  =>  import admin  =>   admin.main()
'''


def main():
    
    ''' Change these fields to create a new admin account'''
    username = "manager"
    password = "welkom1234"
    email = "rensgroot9999@hotmail.com"
    firstname = "rens"
    lastname = "groot"
    
    ''' isadmin needs to be 1 when you create an admin account, take 0 for a normal user '''
    isadmin = 1

    
    ''' Dont change this code below '''
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, email=email, password=hashed_password, firstname=firstname, lastname=lastname, isadmin=isadmin)
    db.session.add(new_user)
    db.session.commit()