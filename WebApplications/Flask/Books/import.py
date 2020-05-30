import csv
import os

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tprfgdhqetvylz:b0b096fe87c132e1a51c3f91d72c50505f6d27a017a544d8c34938d3ecb5cc1a@ec2-54-247-118-139.eu-west-1.compute.amazonaws.com:5432/db66i06oj9aoh2'

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

'''
Open the books.csv file and use the csv-reader to read the file
Insert the isbn, title, author and year into the books database
'''
def main():
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": int(year)})
        
    db.commit()

if __name__ == "__main__":
    main()