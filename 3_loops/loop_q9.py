items = ['apple', 'banana', 'orange', 'apple', 'mango']
for item in items:
    if items.count(item) > 1:
        print(f"Duplicate found: {item}")
        break
