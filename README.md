# Bank Management System

A command-line banking application built with Python and MySQL. Users can create an account, sign in, check their balance, deposit money, withdraw money, and transfer money to another account.

## Features

- Customer registration with a generated account number
- Customer login
- Bank balance enquiry
- Cash deposits
- Cash withdrawals
- Fund transfers
- A separate transaction table for each customer

## Project Structure

| File | Description |
| --- | --- |
| `main.py` | Starts the command-line application and displays the menus |
| `register.py` | Handles sign-up and sign-in workflows |
| `customers.py` | Defines customer creation and inserts customer records |
| `bank.py` | Implements balance enquiries and banking operations |
| `database.py` | Connects to MySQL and creates the customer table |

## Requirements

- Python 3.10 or newer
- MySQL Server
- The Python MySQL Connector package

Install the connector with:

```bash
python -m pip install mysql-connector-python
```

## Database Setup

The application connects to MySQL with the following settings in `database.py`:

```python
host = "localhost"
user = "root"
password = "krish2003"
```

Update these values to match your local MySQL installation before running the application. The program automatically creates and selects the `bank_management_system` database and creates the `customers` table if they do not already exist.

## Run the Application

From the project directory, run:

```bash
python main.py
```

The application first displays:

```text
1. Sign IN
2. Sign UP
```

After signing in, choose one of the available banking operations:

```text
1. Bank Enquiry
2. cash deposit
3. cash withdrawal
4. Fund Transfer
```

## Customer Table

The `customers` table stores:

- Username and password
- Customer name, age, gender, and city
- Account status
- Account number
- Current balance

When a customer registers, the application creates a transaction table named after the customer, using this pattern:

```text
<username>_transactions
```

Each transaction records the date and time, account number, remarks, transaction amount, and resulting balance.

## Notes

- MySQL must be running before starting the application.
- The username is used in dynamically generated transaction-table names. Use simple usernames containing letters, numbers, and underscores.
- The current application uses direct SQL string construction in several places. Parameterized queries should be used before deploying this application outside a local learning environment.
- Passwords are currently stored as plain text. A production application should hash passwords securely.
- The database password is currently stored in `database.py`; use environment variables or a secrets manager for real deployments.
