import re
print("Welcome to Password Strength Checker!")

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1
if re.search("[a-z]", password):
    strength += 1
if re.search("[A-Z]", password):
    strength += 1
if re.search("[0-9]", password):
    strength += 1
if re.search("[!@#$%^&*()_+=-]", password):
    strength += 1

if strength == 5:
    print(" Strong Password!")
elif strength >= 3:
    print(" Medium Password")
else:
    print("Weak Password, try again.")
