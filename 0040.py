# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If d_n represents the nth digit of the fractional part, find the value of the following expression:
# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000 

def champernowne_digit(n):
    length = 0
    digits = 1
    # print(n)
    while length < n:
        length += digits * 9 * 10**(digits - 1)
        # print(length)
        digits += 1
    # print(digits)
    digits -= 1
    length -= digits * 9 * 10**(digits - 1)
    number = 10**(digits - 1) + (n - length - 1) // digits
    return int(str(number)[(n - length - 1) % digits])

product = 1
for i in range(7):
    product *= champernowne_digit(10**i)

print(product)
# 210