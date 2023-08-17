#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")


def takinginputs():
    nr_letters = int(
        input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    return nr_letters, nr_symbols, nr_numbers


def easyPassword(nr_letters, nr_symbols, nr_numbers):
    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    password = ""
    for i in range(0, nr_letters):
        random_letter = random.choice(letters)
        password += random_letter

    for i in range(0, nr_symbols):
        random_symbol = random.choice(symbols)
        password += random_symbol

    for i in range(0, nr_numbers):
        random_number = random.choice(numbers)
        password += random_number

    print(f"\nYour generated password is '{password}'")


def hardPassword(nr_letters, nr_symbols, nr_numbers):
    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    password = ""
    for i in range(0, nr_letters):
        random_letter = random.choice(letters)
        password += random_letter

    for i in range(0, nr_symbols):
        random_symbol = random.choice(symbols)
        password += random_symbol

    for i in range(0, nr_numbers):
        random_number = random.choice(numbers)
        password += random_number
    random_password = ''.join(random.sample(password, len(password)))
    print(f"\nYour generated password is '{random_password}'")


password_type = int(
    input(
        "1. Easy Password \n2. Hard Password \nPress 1 for easy password, 2 for hard password\n"
    ))
if password_type == 1:
    nr_letters, nr_symbols, nr_numbers = takinginputs()
    easyPassword(nr_letters, nr_symbols, nr_numbers)
elif password_type == 2:
    nr_letters, nr_symbols, nr_numbers = takinginputs()
    hardPassword(nr_letters, nr_symbols, nr_numbers)
else:
    print("Enter a valid choice")
