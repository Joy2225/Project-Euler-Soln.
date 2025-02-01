# The problem describes truncatable primes. These are primes that remain prime
# when digits are successively removed from both the left and right ends.
# The example given is 3797.  From left to right: 3797, 797, 97, 7 (all prime).
# From right to left: 3797, 379, 37, 3 (all prime).
#
# The goal is to find all eleven such primes (excluding single-digit primes 2, 3, 5, and 7)
# and calculate their sum.

def is_prime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True

def truncatable(n):
    if not is_prime(n):
        return False
    n = str(n)
    for i in range(1,len(n)):
        if not is_prime(int(n[i:])):
            return False
        if not is_prime(int(n[:i])):
            return False
    return True

n = 11
num = [3, 7, 9]
sum = 0
i = 11
while(n!=0):
    if truncatable(i):
        print(i)
        sum += i
        n -= 1
    i += 2

print(sum)
# 748317