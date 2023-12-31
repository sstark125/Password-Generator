#Password Generator Project
import random
import os
def ConsoleClear():
  os.system('cls' if os.name == 'nt' else 'clear')
ConsoleClear()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

# Populate password string with randomly picked characters
for item in range(nr_letters):
    randLetter = random.randint(0, 51)
    password += letters[randLetter]
    
for item in range(nr_symbols):
    randSymbol = random.randint(0, 7)
    password += symbols[randSymbol]

for item in range(nr_numbers):
    randNum = random.randint(0,8)
    password += numbers[randNum]
    
ConsoleClear()
# Password before Randomization
print(f"Your password: {password}")

# Randomizing the Password
password = ''.join(random.sample(password,len(password)))
print(f"Your randomized password: {password}")
