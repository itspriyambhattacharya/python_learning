def even_generator(n):
    for i in range(2, n+1, 2):
        yield i


for num in even_generator(10):
    for n2 in even_generator(16):
        print(f"Inner: {n2}")
    print(f"Outer num: {num}")
