#Sieve of Eratosthenes algorithm
def f(n):
    primes = []
    sieve = [1] * (n+1)

    for num in range(2, int(n**0.5)+1):
        if sieve[num]:
            for mul in range(num**2, n+1, num):
                sieve[mul] = 0
    for num in range(2, n+1):
        primes.append(num) if sieve[num] else ''
    return primes


#Eratosthenes method
def f(n):
    if n<2:
        return 0
    isPrime = [0,0]+[1]*(n-2)
    for i in range(2, math.ceil(math.sqrt(n))):
        if isPrime[i]:
            for j in range(i*i, n, i):
                isPrime[j] = 0
    return sum(isPrime)



# nth prime number
def nth_prime_no(n):
    if n == 1:
        return n
    prime_list = [2]
    num = 3
    while len(prime_list) < n - 1:
        for i in prime_list:
            if num % i == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


print(nth_prime_no(27))  # 101


# all prime numbers upto n (alternate and efficient)
def get_prime_list(n):
    if n == 1:
        return [1]
    prime_list = [2]
    num = 3
    while prime_list[-1] <= n:
        if num > n:
            break
        for i in prime_list:
            if num % i == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list


print(get_prime_list(20))  # [1, 2, 3, 5, 7, 11, 13, 17, 19]
