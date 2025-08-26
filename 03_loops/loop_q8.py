from math import sqrt
n = int(input("Enter a number: "))
fl = False
for i in range(2, int(sqrt(n)+1), 1):
    if n % i == 0:
        fl = True
        break

if fl == False:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a composite number")
