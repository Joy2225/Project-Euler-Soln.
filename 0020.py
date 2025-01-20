'''Do sum of digits of 100!'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(sum([int(i) for i in str(fact(100))]))
# 648