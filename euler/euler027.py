# author wukat
'''
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive 
values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly 
divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 
80 primes for the consecutive values n = 0 to 79. The product of the 
coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
'''

from euler005 import is_prime

def generate_all_possible_and_logical_pairs(max_abs_a, max_abs_b):
    for b in range(2, max_abs_b + 1):
        if is_prime(b):
            for a in range(-max_abs_a, max_abs_a + 1):
                yield (a, b)

def count_prims(a, b):
    ''' formula is n^2 + an + b '''
    n, act = 0, b
    while act > 0 and is_prime(act):
        n += 1
        act = n*(a + n) + b
    return n

def get_pair_with_biggest_amount_of_primes_from_formula(max_abs_a, max_abs_b):
    max_so_far, pair_product = 0, None
    for (a, b) in generate_all_possible_and_logical_pairs(max_abs_a, max_abs_b):
        temp = count_prims(a, b)
        if temp > max_so_far:
            (max_so_far, pair_product) = (temp, a * b)
    return pair_product

if __name__ == '__main__':
    print(get_pair_with_biggest_amount_of_primes_from_formula(999, 999))
