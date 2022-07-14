import sys
from math import ceil, log2, sqrt

input = sys.stdin.readline

N = int(input())


def prime_factorization(x):
    primes = []
    for i in range(2, int(sqrt(x)) + 1):
        while x % i == 0:
            primes.append(i)
            x //= i
    if x != 1:
        primes.append(x)
    return primes


primes = prime_factorization(N)
print(ceil(log2(len(primes))))
