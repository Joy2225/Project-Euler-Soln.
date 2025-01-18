'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?'''

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 1
    i = 1
    while count < n:
        i += 2
        if is_prime(i):
            count += 1
    return i

print(nth_prime(10001))
# Answer: 104743