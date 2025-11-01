a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b

while y != 0:
    x, y = y, x % y

hcf = x
lcm = (a * b) // hcf

print("HCF:", hcf)
print("LCM:", lcm)
