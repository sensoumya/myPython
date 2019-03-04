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
