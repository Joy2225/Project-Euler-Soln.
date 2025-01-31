# The Fibonacci sequence is defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.
#
# Hence the first 12 terms will be:
# F(1) = 1
# F(2) = 1
# F(3) = 2
# F(4) = 3
# F(5) = 5
# F(6) = 8
# F(7) = 13
# F(8) = 21
# F(9) = 34
# F(10) = 55
# F(11) = 89
# F(12) = 144
#
# The 12th term, F(12), is the first term to contain three digits.
#
# Question: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math

def fn_digit_fibo(n):
    return math.ceil((n-1 + math.log10(5)/2) / math.log10((1+math.sqrt(5))/2))

print(fn_digit_fibo(1000))
# 4782