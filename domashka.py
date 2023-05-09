first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

if first > second:
    gcd = second
else:
    gcd = first
while gcd > 0:
    if first % gcd == 0 and second % gcd == 0:
        print(gcd)
        break
    gcd -= 1

    