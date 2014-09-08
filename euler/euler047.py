# author wukat
'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
from math import sqrt

def get_list_of_prime_factors(number):
    list_of_factors, factor, border, k, d = [], 2, sqrt(number), 1, 1
    while factor < border:
        while number % factor == 0:
            list_of_factors.append(factor)
            number /= factor
        if number == 1:
            break
        if factor >= 3:
            factor = 6 * k + d
            if d == 1:
                d, k = -1, k + 1
            else:
                d = 1
        else:
            factor += 1
    if number != 1:
        list_of_factors.append(number)
    return list_of_factors

def check_if_have_4_distinct_factors(number):
    return True if len(set(get_list_of_prime_factors(number))) == 4 else False

def solve():
    i, count, res = 647, 0, []
    while count < 4:
        if check_if_have_4_distinct_factors(i):
            count += 1
            res.append(i)
        else:
            count = 0
            res = []
        i += 1
    return res

if __name__ == '__main__':
    print(solve())