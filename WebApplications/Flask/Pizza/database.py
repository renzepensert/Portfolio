from models import *
import csv

'''
database.py
Terminal
flask shell
import database
database.main()
ctrl+d to exit shell

'''



def main():
    '''f = open("csv-files/subs.csv")
    reader = csv.reader(f)
    for name, price, price2 in reader:
        sub = Subs(name=name, price=price, price2=price2)
        db.session.add(sub)'''
    
    '''a = open("csv-files/rpizza.csv")
    reader = csv.reader(a)
    for name, price, price2, price3, price4, price5, price6, price7, price8, price9, price10 in reader:
        rpizza = Rpizza(name=name, price=float(price), price2=float(price2), price3=float(price3), price4=float(price4), price5=float(price5), price6=float(price6), price7=float(price7), price8=float(price8), price9=float(price9), price10=float(price10))
        db.session.add(rpizza)'''  
        
    '''b = open("csv-files/spizza.csv")
    reader = csv.reader(b)
    for name, price, price2, price3, price4, price5, price6, price7, price8, price9, price10 in reader:
        spizza = Spizza(name=name, price=price, price2=price2, price3=price3, price4=price4, price5=price5, price6=price6, price7=price7, price8=price8, price9=price9, price10=price10)
        db.session.add(spizza)'''  
    
    '''c = open("csv-files/other.csv")
    reader = csv.reader(c)
    for name, price in reader:
        other = Other(name=name, price=price)
        db.session.add(other)'''
    
    '''d = open("csv-files/platters.csv")
    reader = csv.reader(d)
    for name, price, price2 in reader:
        platters = Platters(name=name, price=price, price2=price2)
        db.session.add(platters)'''
        
    '''e = open("csv-files/toppings.csv")
    reader = csv.reader(e)
    for name, price in reader:
        toppings = Toppings(name=name, price=price)
        db.session.add(toppings)'''
    
    '''g = open("csv-files/extras.csv")
    reader = csv.reader(g)
    for name, price in reader:
        extra = Extras(name=name, price=price)
        db.session.add(extra)'''
    
        
    db.session.commit()