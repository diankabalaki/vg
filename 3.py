import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__}: {end_time - start_time}")
        return result
    return wrapper

@measure_time
def do_some_work():
    time.sleep(3)
    print("good")

do_some_work()