# A simple login system 
username = "deepanshu"
password = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == username and pwd == password:
    print("✅ Login successful! Welcome,", user)
else:
    print("❌ Invalid username or password.")
