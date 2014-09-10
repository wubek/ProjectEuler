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
    return [i for i in range(len(er)) if er[i]]

def make_consecutive_sums_dict(primes_list):
    ''' Returns dictionary having sums of consecutive primes and number of sumed consecutive primes as a value
    ex: primes: [2, 3, 5, 7]
    result {2: 1, 5: 2, 10: 3, 17: 4}
    '''
    actual_sum, actual_counter, result_dict = 0, 0, {}
    for el in primes_list:
        actual_sum += el
        actual_counter += 1
        result_dict[actual_sum] = actual_counter
    return result_dict

def check_length_of_sum_list_of_prime(prime, consecutive_sums_dict, biggest = False):
    '''
    Having prime: 23
    And consecutive_sums_dict: {2: 1, 5: 2, 10: 3, 17: 4, 28: 5}
    Will find: 28 -> 5 and 5 -> 2; return 5 - 2 = 3
    '''
    if prime in consecutive_sums_dict:
        return consecutive_sums_dict[prime]
    elif not biggest:
        actual_val = prime + 1
        while actual_val not in consecutive_sums_dict:
            actual_val += 1
        if actual_val - prime in consecutive_sums_dict:
            return consecutive_sums_dict[actual_val] - consecutive_sums_dict[actual_val - prime]


def solve(limit):
    primes_list = eratosthenes_sieve_compr(limit)
    consecutive_sums_dict = make_consecutive_sums_dict(primes_list)
    act_prime = primes_list[-1]
    longest = check_length_of_sum_list_of_prime(act_prime, consecutive_sums_dict, True)
    if not longest:
        longest = 0
    for i in range(len(primes_list) - 2, 0, -1):
        temp = check_length_of_sum_list_of_prime(primes_list[i], consecutive_sums_dict)
        if temp and temp > longest:
            longest = temp
            act_prime = primes_list[i]
    return act_prime

if __name__ == '__main__':
    # start = datetime.datetime.now()
    print(solve(1000000))
    # print(datetime.datetime.now() - start)