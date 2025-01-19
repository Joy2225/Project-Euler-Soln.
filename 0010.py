'''Sum of all primes below 2 million'''

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    sum = 0
    for p in range(2, n+1):
        if prime[p]:
            sum += p

    print(sum)

if __name__ == '__main__':
    n = 2000000
    SieveOfEratosthenes(n)
# 142913828922