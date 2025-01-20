# Problem 21: Amicable Numbers
#
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair,
# and each of a and b are called amicable numbers.
#
# For example:
# - The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110.
#   Therefore, d(220) = 284.
# - The proper divisors of 284 are 1, 2, 4, 71, and 142.
#   Therefore, d(284) = 220.
#
# Task:
# Evaluate the sum of all the amicable numbers under 10,000.

import math

def sumOfDivisors(x):
    sum_div = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            sum_div += i
            if i != x // i:
                sum_div += x // i
    return sum_div

def findAmicableNumbers(limit):
    amicable_sum = 0
    visited = set()

    for a in range(2, limit):
        if a in visited:
            continue
        b = sumOfDivisors(a)

        if b != a and sumOfDivisors(b) == a:
            amicable_sum += a + b
            visited.add(a)
            visited.add(b)
    
    return amicable_sum

print(findAmicableNumbers(10000))
# 31626