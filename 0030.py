# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Example for fourth powers:
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4

# Note: Numbers like 1 = 1**4 are not considered as they are not a sum.

# Let f(n) be the sum of the fifth powers of the digits of n. 
# The maximum value of f for any k-digit number is 9^5 * k = 59049k, 
# and the minimum value of any k-digit number is 10^(k-1).
# Because 59049k < 10^(k-1) for k > 7, f(n) < n for n > 10^6.
# Also, because f(n) <= 9^5 * 6 = 354294 for n < 10^6, f(n) < n for n >= 354295.


res = 0
for i in range(2, 354294+1):
    if i == sum([int(x)**5 for x in str(i)]):
        res += i
print(res)
# 443839