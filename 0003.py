'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?'''

def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n%2 == 0:
        return False
    for i in range(3,int(n**0.5),2):
        if n%i == 0:
            return False
    return True

def prime_factors(n):
    if is_prime(n):
        return n
    for i in range(2,n):
        if n%i == 0:
            return prime_factors(n//i)

print(prime_factors(600851475143))
# 6857