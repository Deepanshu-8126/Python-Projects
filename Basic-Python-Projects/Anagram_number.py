#anagram number 
str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

if sorted(str1) == sorted(str2):
    print("Both words are Anagrams!")
else:
    print("Not anagrams.")
