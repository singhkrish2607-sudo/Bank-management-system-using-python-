
from database import *

# user register
# create a class for customer
class Customers:
    # create a constructor for customer class
    def __init__(self, username, password, name, age, gender, city, account_number, status=True, balance=0):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__city = city
        self.__status = status
        self.__account_number = account_number
        self.__balance = balance
    # create a method to create a customer in the database
    def create_customer(self):
        cursor.execute(
            """INSERT INTO customers
               (username, password, name, age, gender, city, status, account_number, balance)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (
                self.__username,
                self.__password,
                self.__name,
                self.__age,
                self.__gender,
                self.__city,
                self.__status,
                self.__account_number,
                self.__balance
            ),
        )
        mydb.commit()