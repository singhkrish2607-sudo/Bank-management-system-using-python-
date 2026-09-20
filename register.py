# user register 

from database import *
from customers import *
from bank import Bank
import random

def signUP():
    username = input("Enter your username: ")
    temp = db_query(f"SELECT * FROM customers WHERE username = '{username}';")
    

    if temp:
        print("username is already taken. Please choose a different username.")
        return signUP()
        
    else: 
        print("username is available.")
        password = input("Enter your password: ")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female/other): ")
        city = input("Enter your city: ")
        
        while True:
            account_number = int(random.randint(1000000000, 9999999999))
            temp = db_query(f"SELECT * FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(f"Account number is: {account_number}")
                break

    customer = Customers(
        username, password, name, age, gender, city, account_number,
        status=True, balance=0
    )
    customer.create_customer()

    bank = Bank(username, account_number, 0)
    bank.create_transaction_table()

def signIN():
    username = input("Enter your username: ")
    temp = db_query(f"SELECT username FROM customers WHERE username = '{username}';")
    if temp:
        print(f"Welcome {username} enter your password: ")
        # You can implement the functionality after successful sign-in here
        while True:
            password = input("Enter your password: ")
            temp = db_query(f"SELECT password FROM customers WHERE password = '{password}';")
            if temp:
                print(f"Welcome back to your account! {username}")
                return username
            else:
                print("Incorrect password. Please try again.")
                password
            
    else:
        print("Invalid username. Please try again.")
        return signIN()

