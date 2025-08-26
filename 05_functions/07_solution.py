def sum_all(*args):
    print("*args is ", *args)
    # args in a tuple, an iterable, so we can apple loops and perform other task as well
    print(f"args is {args}")
    for i in args:
        print(i**2)
    return sum(args)


# print(sum_all(1, 2))
print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5))
