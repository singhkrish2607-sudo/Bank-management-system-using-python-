
from register import *
from bank import *


status = False

while True:
   try:
      register = int(input("1. Sign IN\n 2. Sign UP: "))

      if register == 1 or register == 2:
         if register == 2:
            signUP()

         elif register == 1:
            user = signIN()
            status = True
            break
      else:
         print("Invalid input. Please enter 1 or 2.")

   except ValueError:
      print("Invalid input. Please enter a number.")


account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")

account_number = account_number[0][0]
print(f"Your account number is: {account_number}")

while status:
   try:
      facility = int(input("1. Bank Enquiry  \n"
                           "2. cash deposit  \n"
                           "3. cash withdrawal \n"
                           "4. Fund Transfer \n"
                           "select your facility: " 
                           ))

      if facility >= 1 and facility <= 4:
         if facility == 1:
            while True:
               try: 
                  bobj = Bank(user, account_number)
                  bobj.bankEnquiry()
                  break

               except ValueError:
                  print("Invalid input. Enter valid number.")
                  continue
            

         elif facility == 2:
            while True:
               try: 
                  amount = int(input("Enter the amount to deposit: "))
                  bobj = Bank(user, account_number)
                  bobj.deposit(amount)
                  break

               except ValueError:
                  print("Invalid input. Enter valid number.")
                  continue
            

         elif facility == 3:
            while True:
               try: 
                  amount = int(input("Enter the amount to withdraw: "))
                  bobj = Bank(user, account_number)
                  bobj.withdraw(amount)
                  break

               except ValueError:
                  print("Invalid input. Enter valid number.")
                  continue
            


         elif facility == 4:
            while True:
               try: 
                  reciver = int(input("Enter the Reciver account Number: "))
                  amount = int(input("Enter the amount to withdraw: "))
                  bobj = Bank(user, account_number)
                  bobj.transfer(reciver, amount)
                  break

               except ValueError:
                  print("Invalid input. Enter valid number.")
                  continue

      else:
         print("Invalid input. Please select a valid facility.")
   except ValueError:
      print("Invalid input. Please enter a number.")