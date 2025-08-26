n = int(input("Enter a number: "))
i = 1
f = 1
if n == 0:
    print("The factorial of 0 is 1")
    exit()
while (i <= n):
    f = f*i
    i += 1
print(f"The factorial of {n} is {f}")
