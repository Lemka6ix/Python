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
