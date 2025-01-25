# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.  (Meaning, single-digit numbers 1 and 2 are not considered.)

'''
362880*n <= 10^(n-1) 
'''
import math
res = 0
for i in range(10, 7*362880):
    if i == sum(math.factorial(int(digit)) for digit in str(i)):
        res += i
print(res)