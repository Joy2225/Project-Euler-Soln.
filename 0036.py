# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# Note: The palindromic number, in either base, may not include leading zeros.

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_palindrome_base2(n):
    return bin(n)[2:] == bin(n)[2:][::-1]

res = 0
for i in range(1, 1000000):
    if is_palindrome(i) and is_palindrome_base2(i):
        res += i
print(res)
# 872187