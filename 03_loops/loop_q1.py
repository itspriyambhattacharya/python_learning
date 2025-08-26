n = int(input("Enter size of list: "))

lst = []
count = 0  # count of positive numbers

for i in range(n):
    elem = int(input("Enter an element to insert in list: "))
    lst.append(elem)

print(f"The list is: {lst}")
for elem in lst:
    if elem > 0:
        count += 1

print(f"The number of positive numbers present in the list is: {count}")
