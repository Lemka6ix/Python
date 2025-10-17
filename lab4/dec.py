import time

def time_limit(timeout):   #создает и возвращает сам декоратор, timeout - число сек
    def decorator(func):   # func - исходная функция, которую декорируем
        def wrapper(*args, **kwargs):   # args, kwargs - аргументы исходной функции
            start_time = time.time()  # Засекаем время начала выполнения
            result = func(*args, **kwargs)    # вызываем исходную функцию с её оригинальными аргументами 
            end_time = time.time()   # Засекаем время окончания выполнения
            if end_time - start_time > timeout:
                raise TimeoutError("Function exceeded time limit")
            return result
        return wrapper
    return decorator

def create_prime_finder():
    primes_cache = {}  # Кэш для хранения результатов
    
    @time_limit(1)
    def get_primes(n):
        if n in primes_cache:
            return primes_cache[n]
        
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        
        primes_cache[n] = primes
        return primes
    
    return get_primes


prime_finder = create_prime_finder()  

try:
    primes = prime_finder(100000)  
    print(primes)
except TimeoutError:
    print("Функция превысила лимит времени")