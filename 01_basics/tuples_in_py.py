print('================================================ Tuples Introduction ================================================')

tup1 = (0, 1, 2, 3, 4, 5)
print(tup1)
print(f"The first element is  {tup1[0]}")
print(f"The last element is  {tup1[-1]}")
try:
    tup1[1] = 67  # error
except TypeError:
    print("TypeError Occured while executing tup1[1]=67")

print(f"The length of the tuple is: {len(tup1)}")

tup2 = (9, 8, 7)
tup_all = tup1+tup2
print(tup_all)

if 5 in tup_all:
    print("Success")
else:
    print("Absent")

tup3 = (1, 2, 2, 2, 3, 4, 4, 3, 7, 7)
print(tup3.count(3))

print('================================================ Unpacking Tuples ================================================')
t1 = (1, 2, 3)

try:
    (one, two) = t1
    print(one)
    print(two)
except ValueError:
    print("Value Error occured during Unpacking due to too few arguments")

try:
    (one, two, three) = t1
    print(one)
    print(two)
    print(three)
except ValueError:
    print("Value Error occured during Unpacking due to too few arguments")
