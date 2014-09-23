# author wukat
'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them 
in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest 
sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which 
any two primes concatenate to produce another prime.
'''

from euler050 import eratosthenes_sieve_compr

def check_primality(num, primes):
    limit = num ** (0.5)
    for prime in primes:
        if prime >= limit:
            return True
        if num % prime == 0:
            return False
    return True

def check_pair(prime1, prime2, primes):
    str1, str2 = str(prime1), str(prime2)
    if check_primality(int(str1 + str2), primes):
        if check_primality(int(str2 + str1), primes):
            return True

def make_pairs_dict(primes):
    dict_pairs, limit = {}, len(primes),
    for i in primes:
        dict_pairs[i] = set()
    for i in range(limit - 1):
        for j in range(i + 1, limit):
            if check_pair(primes[i], primes[j], primes):
                dict_pairs[primes[i]].add(primes[j])
    return dict_pairs

def solve(limit):
    primes = eratosthenes_sieve_compr(limit)[1:] # without 2
    min_so_far, dict_pairs = float("infinity"), make_pairs_dict(primes)

    for i in primes[:-4]:
        for j in dict_pairs[i]:
            for k in dict_pairs[i] & dict_pairs[j]:
                for l in dict_pairs[i] & dict_pairs[j] & dict_pairs[k]:
                    for m in dict_pairs[i] & dict_pairs[j] & dict_pairs[k] & dict_pairs[l]:
                        sum_temp = i + j + k + l + m 
                        print(i, j, k, l, m)
                        if sum_temp < min_so_far:
                            min_so_far = sum_temp
    return min_so_far


if __name__ == '__main__':
    print(solve(9000))


