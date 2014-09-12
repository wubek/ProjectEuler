# author wukat
'''
It was proposed by Christian Goldbach that every odd composite 
number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written 
as the sum of a prime and twice a square?
'''

from euler005 import is_prime

def check_if_can_be_represented(number):
    i = 1
    while 2 * i ** 2 < number - 2:
        if is_prime(number - 2 * i ** 2):
            return True
        i += 1

def solve():
    i = 9
    while check_if_can_be_represented(i):
        i += 2
        while is_prime(i):
            i += 2
    return i

if __name__ == '__main__':
    print(solve())