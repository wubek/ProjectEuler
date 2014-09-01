# author wukat
'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from euler005 import is_prime

def check_number(number):
    if not is_prime(number):
        return False
    for i in range(1, len(str(number))):
        if not is_prime(number // 10**i) or not is_prime(number % 10**i):
            return False
    return True

def get_sum_of_special_primes():
    found, sum_of_special_primes, number = 0, 0, 23
    while found < 11:
        if check_number(number):
            sum_of_special_primes += number
            found += 1
        number += (6 if number % 10 == 7 else 2)
    return sum_of_special_primes


if __name__ == '__main__':
    print(get_sum_of_special_primes())