# author wukat
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

def is_pandigital_str(str_number, n):
    used, to_use = set(), set(str(i) for i in range(1, n + 1))
    for digit in str_number:
        if digit in to_use and digit not in used:
            used.add(digit)
        else:
            return False
    return not (to_use - used)

def find_proper_numbers():
    proper_pairs_and_product = []
    for first in range(2, 99):
        second = 100
        product = second * first
        while product < 10000:
            product = second * first
            proper_pairs_and_product.append((first, second, product))
            second += 1
    return proper_pairs_and_product

def sum_up_proper_panadigitals(proper_pairs_and_product):
    set_of_products = set()
    for first, second, product in proper_pairs_and_product:
        if is_pandigital_str(str(first) + str(second) + str(product), 9):
            set_of_products.add(product)
    return sum(set_of_products)

if __name__ == '__main__':
    print(sum_up_proper_panadigitals(find_proper_numbers()))
