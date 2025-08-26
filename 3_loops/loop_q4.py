str1 = input("Enter a string: ").strip()
t = ""

for i in range(0, len(str1)):
    ch = str1[i]
    t = ch+t
print(f"The reversed string is: {t}")
