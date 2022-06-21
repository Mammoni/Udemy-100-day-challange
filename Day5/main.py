#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def easy_password(nr_letters,nr_symbols,nr_numbers,letters,numbers,symbols):
  #Eazy Level - Order not randomised:
  #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
  password = ""
  for char in range(1,nr_letters+1):
    password += random.choice(letters)
  for char in range(1,nr_symbols+1):
    password += random.choice(symbols)
  for char in range(1,nr_numbers+1):
    password += random.choice(numbers)

  print(f'Easy password for you is: {password}')
  
def hard_pass(nr_letters,nr_symbols,nr_numbers,letters,numbers,symbols):
  #Hard Level - Order of characters randomised:
  #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
  password = ""
  password_list = []
  for char in range(1,nr_letters+1):
    password_list += random.choice(letters)
  for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)
  for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

  random.shuffle(password_list)

  for char in password_list:
    password += char
    
  print(f'Hard password for you is: {password}')


print("Welcome to the PyPassword Generator!")
version = input("What type of password do you want?\n")
if(version.lower() == 'easy'):
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  easy_password(nr_letters,nr_symbols,nr_numbers,letters,numbers,symbols)
elif version.lower() == 'hard':
  nr_letters= int(input("How many letters would you like in your password?\n")) 
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))
  hard_pass(nr_letters,nr_symbols,nr_numbers,letters,numbers,symbols)
else:
  print('Wrong input!!!')
