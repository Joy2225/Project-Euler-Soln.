# Find the product of the coefficients, a and b, for the quadratic expression n² + an + b that produces the maximum number of primes for consecutive values of n, starting with n = 0, where |a| < 1000 and |b| ≤ 1000.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def quadratic_primes():
    max_primes = 0
    product = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if is_prime(abs(b)):
                n = 0
                while True:
                    quadratic = n**2 + a*n + b
                    if not is_prime(quadratic):
                        break
                    n += 1
                if n > max_primes:
                    max_primes = n
                    product = a * b
    return product

print(quadratic_primes())
# -59231