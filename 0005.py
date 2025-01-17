'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''

def LCM(a, b):
    greater = max(a, b)
    smallest = min(a, b)
    for i in range(greater, a*b+1, greater):
        if i % smallest == 0:
            return i

res = 1

for i in range(2, 21):
    res = LCM(res, i)

print(res)
# 232792560