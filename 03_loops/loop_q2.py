n = int(input("Enter a number: "))
sum = 0
for i in range(n+1):
    if (i % 2 == 0):
        sum += i
print(f"The sum is {sum}")
