# Вариант 12
## Задание 1
Замыкание для получения простых чисел.

## Решение 
```python
def create_prime_finder():
    primes_cache = {}  # Кэш для хранения результатов
    
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
print(prime_finder(100))
```
* Вызывается create_prime_finder()
* Создается пустой словарь primes_cache = {}
* Возвращается функция get_primes (но она пока не выполняется!)
* prime_finder теперь ссылается на функцию get_primes

* внутренняя функция `get_primes` замыкает на себе переменную `primes_cache` из внешней функции `create_prime_finder`, и эта переменная живет столько, сколько живет сама `get_primes`.

## Результат выполнения

![result1](https://github.com/Lemka6ix/Python/blob/main/lab4/zam.png)


## Задание 2
Декоратор, не позволяющий функции выполняться больше определённого времени.
## Решение
```python
import time


def time_limit(timeout):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)  
            end_time = time.time()
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
```

* Начинаем замер времени → `start_time = time.time()`
* Запускаем исходную функцию → `result = get_primes(100000)`
* Останавливаем секундомер → `end_time = time.time()`
* Проверяем не превысили ли лимит → `if end_time - start_time > 1`
* Если превысили — кричим "СТОП!" → `raise TimeoutError`

## Результат выполнения
![result2](https://github.com/Lemka6ix/Python/blob/main/lab4/dec.png)
