# author wukat
'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
# they probably think of the longest sum of consecutive primes
import datetime
from math import sqrt
from euler010 import eratosthenes_sieve

def eratosthenes_sieve_compr(limit):
    er = eratosthenes_sieve(limit)
    return {i for i in range(len(er)) if er[i]}

def solve(limit):
    primes_set = eratosthenes_sieve_compr(limit)
    primes_list = list(primes_set)
    primes_list.sort()
    begin_len = len(primes_set) - 1
    for length in range(begin_len, 1, -1):
        for j in range(begin_len - length + 1):
            if sum(primes_list[j : j+length]) in primes_set:
                return sum(primes_list[j : j+length])

if __name__ == '__main__':
    start = datetime.datetime.now()
    print(solve(1000000))
    print(datetime.datetime.now() - start)