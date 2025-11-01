word = input("Enter a word: ")
reverse = ""

for ch in word:
    reverse = ch + reverse

if word == reverse:
    print("It's a palindrome!")
else:
    print(" Not a palindrome.")
