l1 = ["Hello", 'Priyam', 'world', 'go', 'great', 'hello world', 'bhattacharya']
print(l1)
print(l1[1:4])
l1[1:2] = "hello2"  # problem
print(l1)
l1 = ["Hello", 'Priyam', 'world', 'go', 'great', 'hello world', 'bhattacharya']
l1[1:2] = ["hello2"]  # solution
print(l1)

l1[1:3] = ['hello5', 'priyam5']
print(l1)

lst = [1, 2, 3, 4, 5, 6]
lst[1:3] = [22, 33]
print(lst)

print(lst[1:1])
lst[1:1] = ["t1", "t2"]
print(lst)

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst[1:3] = []
print(lst)

# Intro to loops and conditions

lst = [0, 1, 2, 3]

for i in lst:
    print(i)

for i in lst:
    print(i, end=" -> ")

if 34 in lst:
    print("Yes exists")
else:
    print("No, doesn't exists")


lst = [1, 2, 3, 4]
print(lst)
lst.append(55)
print(lst)
x = lst.pop()
print(f"x is {x} and lst is {lst}")
y = lst.remove(4)
print(f"y is {y} and lst is {lst}")
print(lst)

lst2 = lst  # same memory location is shared between lst and lst2
print("lst2 is", lst2)
lst.insert(3, 77)
print("Inserted successfully")
print(f"lst is {lst}")
print(f"lst2 is {lst2}")
# THis problem can be solved in the following way

print(lst)
lst2copy = lst.copy()  # separate memory location is created
lst.pop()
print(lst)
print(lst2copy)
lst.insert(88, 100)
print(lst)
print('================================================ List Comprehension ================================================')

lComp1 = [i for i in range(1, 11)]
print(lComp1)

lComp2 = [i+1 for i in range(10)]
print(lComp2)

lComp3 = [i*6 for i in range(10)]
print(lComp3)
