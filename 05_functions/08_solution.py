def print_items(**kwargs):
    for key, value in kwargs.items():
        print(f"Key is {key} and value is {value}")


print_items(name="Priyam Bhattacharya")
print_items(name="Priyam Bhattacharya", age=24)
