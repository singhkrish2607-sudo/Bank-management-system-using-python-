from database import *
import datetime


class Bank:
    def __init__(self, username, account_number, balance=0):
        self.__username = username
        self.__account_number = account_number
        self.__balance = balance

        # create a function for create a transaction table for each customer
        self.create_transaction_table


    # create a finction for create a each customer name transaction table  in the database
    def create_transaction_table(self):
        db_query(f"""
            CREATE TABLE IF NOT EXISTS {self.__username}_transactions (
                Datetime DATETIME DEFAULT CURRENT_TIMESTAMP,
                account_number VARCHAR(20),
                remarks VARCHAR(100),
                amount int,
                balance int 
            )
            """)
        

    # create a function for bank enquiry and display the balance of the customer
    def bankEnquiry(self):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")

        # check if the account was found
        if temp:
            print(f"Current balance: {temp[0][0]}")
        else:
            print("Account was not found.")

    # create a function for deposit money in the customer account and update the balance in the transaction table
    def deposit(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")

        # Add the deposit amount to the current balance
        new_amount = temp[0][0] + amount

        # Update the balance in the customers table
        db_query(f"UPDATE customers SET balance = {new_amount} WHERE username = '{self.__username}';")

        # use the bankEquiry function for the store the transaction in the user transaction table  
        self.bankEnquiry()
        db_query(f"""insert into {self.__username}_transactions values (
                '{datetime.datetime.now()}', 
                '{self.__account_number}',
                'Amount Deposit',
                '{amount}',
                '{new_amount}'
                )""")
        print(f"Amount: {amount} is succefully Deposit in your account: {self.__account_number} ")
        mydb.commit()



    # Create a function for withdraw money in the customer self account  
    def withdraw(self, amount):
        temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")

        balance = temp[0][0]

        if amount < balance :
            # Add the withdraw amount to the current balance
            new_amount = balance - amount
    
            # Update the balance in the customers table
            db_query(f"UPDATE customers SET balance = {new_amount} WHERE username = '{self.__username}';")
             # use the bankEquiry function for the store the transaction in the user transaction table  
            self.bankEnquiry()
            db_query(f"""insert into {self.__username}_transactions values (
                    '{datetime.datetime.now()}', 
                    '{self.__account_number}',
                    'Amount Withdrow',
                    '{amount}',
                    '{new_amount}'
                    )""")
            print(f"You amount: {amount} is succefully withdraw in your bank account: {self.__account_number} ")
        else: 
            print(f"Sorry! Your given Amount: {amount}  is higher than the your account Balance. ")
        mydb.commit()



    # create a function for transfer money in you account to another account.
    def transfer(self, reciver,  amount):
            temp = db_query(f"SELECT balance FROM customers WHERE username = '{self.__username}';")
    
            deduct_balance = temp[0][0]
            
    
            if amount < deduct_balance :
                temp2 = db_query(f"SELECT username, balance FROM customers WHERE account_number = '{reciver}';")
                reciver_username = temp2[0][0] 
                add_balance = temp2[0][1]

                # Add the withdraw amount to the current balance
                deduct_amount = deduct_balance - amount
                add_amount = add_balance + amount
                        
                # Update the balance in the customers table
                db_query(f"UPDATE customers SET balance = {deduct_amount} WHERE username = '{self.__username}';")
                
                 # use the bankEquiry function for the user transfer amount store the transaction.  
                self.bankEnquiry()
                db_query(f"""insert into {self.__username}_transactions values (
                        '{datetime.datetime.now()}', 
                        '{self.__account_number}',
                        'Fund Deduct from {self.__username}',
                        '{amount}',
                        '{deduct_amount}'
                        )""")

                # reciver table transaction storing data 
                
                db_query(f"UPDATE customers SET balance = {add_amount} WHERE account_number = '{reciver}';")
                # use the bankEquiry function for the store the transaction in the user transaction table  
                
                self.bankEnquiry()
                db_query(f"""insert into {reciver_username}_transactions values (
                           '{datetime.datetime.now()}', 
                           '{self.__account_number}',
                           'Fund Transfer to {reciver_username} ',
                           '{amount}',
                           '{add_amount}'
                           )""")

                
                print(f"₹{amount} was successfully transferred to account: {reciver}")

            else:
                print(f"Sorry! Your given amount: {amount} is higher than your account balance: {deduct_balance}")

    mydb.commit()