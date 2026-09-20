import mysql.connector as mysql

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="krish2003",
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS bank_management_system")
cursor.execute("USE bank_management_system")


def createcustomer():
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    username varchar(20) primary key,
                    password VARCHAR(20),
                    name VARCHAR(100),
                    age int,
                    gender enum('male', 'female', 'other'),
                    city varchar(100),
                    status boolean default True,
                    account_number varchar(20),
                    balance int 
                    )""")
    mydb.commit()

createcustomer()

def db_query(query):
     cursor.execute(query)
     return cursor.fetchall()

     



                                