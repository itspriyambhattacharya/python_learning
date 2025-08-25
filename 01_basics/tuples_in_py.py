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
