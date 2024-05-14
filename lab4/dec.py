def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num*0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

import time

def time_limit(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, *kwargs)
            end_time = time.time()
            if end_time - start_time > timeout:
                raise TimeoutError("Function exceeded time limit")
            return result
        return wrapper
    return decorator

timeout = 2

timed_get_primes = time_limit(timeout)(get_primes)

try:
    primes = timed_get_primes(1000)
    print(primes)
except TimeoutError:
    print("Функция превысила лимит времени")
