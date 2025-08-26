s1 = input("Enter a string: ").strip()
size = len(s1)
fl = False
idx = 0
for i in range(0, size, 1):
    if ((s1[i] not in s1[0: i]) and (s1[i] not in s1[i+1:])):
        fl = True
        idx = i
        break
if fl == True:
    print(f"The first non-repeating character is {s1[idx]}")
else:
    print("Nothing found")
