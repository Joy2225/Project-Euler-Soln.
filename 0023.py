# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.Lesser than 28123.

import math

def sumOfDivisors(x):
    sum_div = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            sum_div += i
            if i != x // i:
                sum_div += x // i
    return sum_div

def findAbundantNumbers(limit):
    abundant_numbers = set()
    for i in range(12, limit):
        if sumOfDivisors(i) > i:
            abundant_numbers.add(i)
    return abundant_numbers

def findNonAbundantSum(limit):
    abundant_numbers = findAbundantNumbers(limit)
    non_abundant_sum = 0
    for i in range(1, limit):
        for abundant in abundant_numbers:
            if i - abundant in abundant_numbers:
                break
        else:
            non_abundant_sum += i
    return non_abundant_sum

print(findNonAbundantSum(28123))
# 4179871