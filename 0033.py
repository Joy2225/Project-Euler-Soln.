from fractions import Fraction

'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the
numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def is_curious_fraction(numerator, denominator):
    num_str = str(numerator)
    den_str = str(denominator)
    
    if '0' in num_str or '0' in den_str:
        return False
    
    for digit in num_str:
        if digit in den_str:
            new_num_str = num_str.replace(digit, '', 1)
            new_den_str = den_str.replace(digit, '', 1)
            if new_den_str != '0' and new_num_str != '0':
                if int(new_num_str) * denominator == int(new_den_str) * numerator:
                    return True
    return False

product = Fraction(1, 1)

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        if is_curious_fraction(numerator, denominator):
            product *= Fraction(numerator, denominator)

print(product.denominator)
# 100