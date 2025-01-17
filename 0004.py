'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product():
    for high in range(999, 99, -1):
        palindrome = int(str(high) + str(high)[::-1])
        for divisor in range(999, 99, -1):
            if palindrome % divisor == 0:
                quotient = palindrome // divisor
                if 100 <= quotient <= 999:
                    return palindrome
    return None

print(largest_palindrome_product())
