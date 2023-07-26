#How We Can Form A Triangle With 3 num#
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a < b + c:
    Check ="Triangle Can Be Form"
else:
    Check ="Triangle Cant Be Form"

if b < a + c:
    Check ="Triangle Can Be Form"
else:
    Check="Triangle Cant Be Form"

if c < a + b:
    Check ="Triangle Can Be Form"
else:
    Check ="Triangle Cant Be Form"

print(Check)