fruit = input("Enter fruit name:").strip().lower()

if fruit == "banana":
    fruit_color = input("Enter colour of the fruit: ").strip().lower()
    if fruit_color == "green":
        print("Unripe")
    elif fruit_color == "yellow":
        print("Ripe")
    elif fruit_color == "brown":
        print("Overripe")
else:
    print("Status Not Available....")
