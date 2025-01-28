# How many circular primes are there below one million?
def is_prime(n):
  if n!=2 and n%2==0:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def rotations(n):
  s = str(n)
  return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n):
  return all(is_prime(r) for r in rotations(n))

count = 0 
limit = 1000000

for i in range(3, limit,2):
  if is_prime(i) and is_circular_prime(i):
    count += 1

print(count+1)
# 55