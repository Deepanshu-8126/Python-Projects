num = int(input("Enter a number: "))
a = num
total = 0

while temp > 0:
    digit = a % 10
    total += digit ** 3
    a //= 10

if total == num:
    print(num, "is an Armstrong number ")
else:
    print(num, "is not an Armstrong number ")
