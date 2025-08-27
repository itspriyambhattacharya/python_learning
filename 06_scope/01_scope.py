x = 23


def f1():
    global x
    x = 56


f1()
print(f"Global x is: {x}")


def dummy(num):
    def actual(n):
        return n**num
    return actual


f = dummy(2)
g = dummy(3)
print(f)
print(f(4))
