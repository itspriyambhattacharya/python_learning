age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
price = 0
if (age >= 18):
    price = 12
else:
    price = 8

if day == 'wednesday':
    price -= 2

print(f"The price is: {price}")
