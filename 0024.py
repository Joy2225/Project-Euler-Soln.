'''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_permutation(digits, n):
    permutation = []
    k = n - 1
    while digits:
        f = factorial(len(digits) - 1)
        print(f)
        index = k // f
        permutation.append(digits.pop(index))
        k %= f
    return ''.join(permutation)

print(get_permutation(list('0123456789'), 1000000))
# 2783915460    