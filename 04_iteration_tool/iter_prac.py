myList = [1, 2, 3, 4]

I = iter(myList)
print(I)

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
# print(I.__next__()) StopIteration

try:
    print(I.__next__())
except StopIteration:
    print("Exception Occured")

myDict = {
    'a': 1, 'b': 2
}

I2 = iter(myDict)
print(I2)
print(I2.__next__())
print(next(I2))
try:
    print(next(I2))

except StopIteration:
    print("Exception Occured, reached end of dictionary")
