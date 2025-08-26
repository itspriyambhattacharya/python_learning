n = int(input("Enter the number to calculate the multiplication table: "))
print(
    f"============================== THe Multiplicaation Table of {n} is ==============================")

for i in range(1, 11, 1):
    if i == 5:
        continue
    print(f"{n} X {i} = {n*i}")
