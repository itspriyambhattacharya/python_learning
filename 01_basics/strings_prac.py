s1 = '0123456789'
# string slicing
print(s1[:])
print(s1[1:5])
print(s1[1:1])
print(s1[1:2])
print(s1[6:1])
print(s1[-6:-1])
print(s1[2:8:1])
print(s1[2:8:2])
print(s1[-8:-2:2])


s2 = "hello world     "
print("Length of s2 is ", len(s2))
print(s2.lower())
print(s2.upper())

s3 = s2.strip()  # similar to trim
print(s3, len(s3))

s3 = "let's go"
s4 = "let's go go go"
print(s3.replace("go", "don't go"))
print(s4.replace("go", "don't go"))

s4 = "0,1,2,3,4,5,6,7,8,9,10"
s5 = s4.split(",")
print(s5)

print("Good weather weather".find("weather"))
s4 = "let's go go go"
print(s4.count("go"))

name = 'Priyam Bhattacharya'
age = 24

print("My name is {} and age is {}years".format(name, age))
print(f"My name is {name} and age is {age}years.")

# Converting string to lisst
s1 = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
ls1 = s1.split(", ")
print(ls1)
s2 = "".join(ls1)  # basic joining
print(s2)
s2 = ", ".join(ls1)  # basic joining
print(s2)
