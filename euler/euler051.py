# author wukat
'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number 
is the first example having seven primes among the ten generated numbers, yielding the 
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being 
the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent 
digits) with the same digit, is part of an eight prime value family.
'''

from euler050 import eratosthenes_sieve_compr
from euler005 import is_prime
from itertools import combinations

def find_primes_families():
    pass

def repr_number_as_list(number):
    ''' 123 => [1, 2, 3] '''
    return map(lambda digit: ord(digit) - ord("0"), str(number))

def make_num_from_list_repr(list_repr):
    ''' [1, 2, 3] => 123 '''
    number, counter = 0, 0
    for el in reversed(list_repr):
        number += el * 10 ** counter
        counter += 1
    return number

def make_list_of_lists_of_digit_positions(number):
    ''' Position counted from right
    1109545 => [[4], [6, 5], [], [], [1], [2, 0], [], [], [], [3]]
    '''
    number_as_list, list_of_lists_of_digit_positions = repr_number_as_list(number), [[] for i in range(10)]
    for i in range(len(number_as_list)):
        list_of_lists_of_digit_positions[number_as_list[i]].append(len(number_as_list) - i - 1)
    return list_of_lists_of_digit_positions

def is_primes_family(prime):
    pass

if __name__ == '__main__':
    # print(find_primes_families())
    # print(is_primes_family(56003))
    print(eratosthenes_sieve_compr(9999))