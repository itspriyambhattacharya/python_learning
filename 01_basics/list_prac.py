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
