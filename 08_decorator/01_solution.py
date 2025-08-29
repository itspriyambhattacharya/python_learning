import time


def timer(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return res
    return wrapper


@timer
def example_func(n):
    time.sleep(n)


example_func(2)
