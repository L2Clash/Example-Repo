import mysql.connector
from Keys.Codes import *
import random

def createAccount():
    while True:
        name1 = input("Please input your first name: ")
        if len(name1) == 0:
            print("Ensure you have entered your name")
            continue
        name2 = input("Please input your last name: ")
        if len(name2) == 0:
            print("Ensure you have entered each name")
            continue
        break
    while True:
        ssn = input("Please input your social security number: ")
        if ((len(ssn) != 9 )or not (ssn.isdigit())):
            print("Please input a valid 9 digit Social Security Number")
            continue
        else:
            break
    while True:
        pin = input("Please input your 4 digit password to approve transactions: ")
        if ((len(pin) != 4) or not (pin.isdigit())):
            continue
        else:
            break
    accept = input(
        f"\nPlease confirm the following data is correct (Y/N): \n"
        f'Name: {name1} {name2}\n'
        f'SSN: {ssn}\n'
        f'Pin #: {pin}\n'
                   )
    if accept.lower() in ['yes', 'y']:
        addData = (f"INSERT INTO bank_data (account_id, account_pin, acc_balance, first_name, last_name, ssn, routing_num) VALUES (0, {pin}, 0.00, '{name1}', '{name2}', {ssn}, {random.randint(10000000, 10099999)});")
        cursor.execute(addData)
        connection.commit()
        query = (f"SELECT account_id, routing_num FROM bank_data WHERE ssn = {ssn};")
        cursor.execute(query)
        for data in cursor:
            entry1 = data[0]
            entry2 = data[1]
        print(f"\nYour Bank Info: \n"
          f"Account #: {entry1}\n"
          f"Routing #: {entry2}")
    else:
        createAccount()

def sign_In():
    while True:
        while True:
            input_Id = input("Please enter your account ID: ")
            if ((len(input_Id) != 6) or not (input_Id.isdigit())):
                print("Please ensure you are inputting your correct account ID")
                continue
            else:
                break
        while True:
            account_Pin = input("Please input your account pin: ")
            if ((len(account_Pin) != 4) or not (input_Id.isdigit())):
                print("Please input a valid 4 digit pin")
                continue
            else:
                break

        query = (f"SELECT * FROM bank_data WHERE account_id = {input_Id} and account_pin = {account_Pin};")
        cursor.execute(query)
        for item in cursor:
            acc_id = item[0]
            pin = item[1]
            bal = item[2]
            name_one = item[3]
            name_two = item[4]
            ssn = item[5]
            routing = item[6]
        return acc_id, pin, bal, name_one, name_two, ssn, routing
        

def add_money(id, balance):
    while True:
        deposit = input("Enter the amount of money you are depositing into your account(---x.xx): ")
        if (is_Monetary(deposit)):
            add_Money = (f"UPDATE bank_data SET acc_balance = {float(balance) + float(deposit)} WHERE account_id = {id}")
            cursor.execute(add_Money)
            connection.commit()

            display = (f"SELECT first_name, last_name, acc_balance FROM bank_data WHERE account_id = {id};")
            cursor.execute(display)
            for item in cursor:
                print(item)
            break
        else:
            print("Please input a correct monetary display (--x.xx)")

def remove_money(id, balance):
    while True:
        deposit = input("Enter the amount of money you are withdrawing into your account(---x.xx): ")
        if (is_Monetary(deposit)):
            add_Money = (f"UPDATE bank_data SET acc_balance = {float(balance) - float(deposit)} WHERE account_id = {id}")
            cursor.execute(add_Money)
            connection.commit()

            display = (f"SELECT first_name, last_name, acc_balance FROM bank_data WHERE account_id = {id};")
            cursor.execute(display)
            for item in cursor:
                print(item)
            break
        else:
            print("Please input a correct monetary display (--x.xx)")

def change_name(id):
    while True:
        deposit = input("Enter what you are changing your first name to(Enter null if no change): ")
        if (len(deposit) > 0):
            change_first = (f"UPDATE bank_data SET first_name = '{deposit}' WHERE account_id = {id};")
            cursor.execute(change_first)
            connection.commit()

            display = (f"SELECT first_name, last_name FROM bank_data WHERE account_id = {id};")
            cursor.execute(display)
            for item in cursor:
                print(item)
        elif (deposit == ''):
            break

        deposit = input("Enter what you are changing your last name to(Enter null if no change): ")
        if (len(deposit) > 0):
            change_last = (f"UPDATE bank_data SET last_name = '{deposit}' WHERE account_id = {id};")
            cursor.execute(change_last)
            connection.commit()

            display = (f"SELECT first_name, last_name FROM bank_data WHERE account_id = {id};")
            cursor.execute(display)
            for item in cursor:
                print(item)
        elif (deposit == ''):
            break
        break

def is_Monetary(user_input):
    if("." not in user_input):
        return False
    check1 = user_input.lstrip()
    check2 = check1.rstrip()
    check3 = check2.split('.')
    return (((check3[0].isdigit()) and ((check3[1].isdigit()))) and (len(check3[1]) == 2))

def check_balance(acc_id):
    display = (f"SELECT first_name, last_name, acc_balance FROM bank_data WHERE account_id = {acc_id}")
    cursor.execute(display)
    for item in cursor:
        print(item)


connection = mysql.connector.connect(user = userkey, database = dbkey, password = passkey)
cursor = connection.cursor(buffered = True)

print("Hello! Welcome to Austyssa Banking")

while True:
    action = input("Sign In or Create an Account: ")
    if action.lower() in ["sign in", "login", "log in"]:
        choice = True
        break
    elif action.lower() in ["create an account", "create"]:
        choice = False
        break
    else:
        print("Please enter 'sign in' or 'create'")

if not choice:
    createAccount()
    result = sign_In()
    print(f"{result[3]} {result[4]} signed in")
elif choice:
    result = sign_In()
    print(f"{result[3]} {result[4]} signed in")

while True:
    number_choice = 0
    while True:
        new_choice = input("Choose to deposit[1], withdraw[2], check balance[3], update name[4], or end session[5]")
        if new_choice.lower() in ["deposit", "1", "one" ]:
            number_choice = 1
            break
        elif new_choice.lower() in ["withdraw", "2", "two"]:
            number_choice = 2
            break
        elif new_choice.lower() in ["check balance", "check", "balance", "3", "three"]:
            number_choice = 3
            break
        elif new_choice.lower() in ["update name", "update", "name", "4", "four"]:
            number_choice = 4
            break
        elif new_choice.lower() in ["end session", "end", "session", "5", "five"]:
            number_choice = 5
            break
        else:
            print("Please enter 'deposit', 'withdraw', 'check balance', or 'update name'")

    if number_choice == 1:
        add_money(result[0], result[2])
    elif number_choice == 2:
        remove_money(result[0], result[2])
    elif number_choice == 3:
        check_balance(result[0])
    elif number_choice == 4:
        change_name(result[0])
    elif number_choice == 5:
        break

cursor.close()
connection.close()