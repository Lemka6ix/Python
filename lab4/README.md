# Вариант 12
## Задание 1
Замыкание для получения простых чисел.

## Решение 
```python
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


primes = get_primes(10)
print(primes)
```
* Создаёт пустой список `primes` для хранения простых чисел.
* Перебирает числа от 2 до `n` с помощью цикла `for`.
* Для каждого числа `num` в этом диапазоне оно проверяет, является ли оно простым.
* Если `num` является простым, оно добавляется в список `primes`.
* После перебора всех чисел в диапазоне замыкание возвращает список `primes`.

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
            result = func(*args, *kwargs)
            end_time = time.time()
            if end_time - start_time > timeout:
                raise TimeoutError("Function exceeded time limit")
            return result
        return wrapper
    return decorator


@time_limit(1)
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


try:
    primes=get_primes(10000)
    print(primes)
except TimeoutError:
    print("Функция превысила лимит времени")
```
* Декоратор `time_limit` принимает аргумент `timeout`, который указывает лимит времени для выполнения функции.
* Возвращает декоратор, который принимает функцию в качестве аргумента.
* Вложенная функция `wrapper` вызывает декорированную функцию и измеряет время выполнения.
* Если время выполнения превышает `timeout`, выбрасывается исключение `TimeoutError`.
* В противном случае возвращается результат вызова декорированной функции.
* Устанавливает лимит времени для функции `get_primes` в 2 секунды.
* Декорирует функцию `get_primes` декоратором `time_limit`, создавая `timed_get_primes`.
* Пытается получить простые числа до 1000 с использованием `timed_get_primes`.
* Если время выполнения превышает лимит, печатает "Функция превысила лимит времени".
* Иначе печатает список простых чисел.

## Результат выполнения
![result2](https://github.com/Lemka6ix/Python/blob/main/lab4/dec.png)
