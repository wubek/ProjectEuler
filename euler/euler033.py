# author wukat
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

def simplify_fraction_incorectly(numerator, denominator):
    ''' two-digital numbers only '''
    first, second = (numerator // 10, numerator % 10), (denominator // 10, denominator % 10)
    if numerator == denominator or (first[0] == second[1] and first[1] == second[0]):
        return False
    else:
        for i in range(2):
            if first[i] == second[(i + 1) % 2]:
                return (first[(i + 1) % 2], second[i])
            if first[i] == second[i]:
                return (first[(i + 1) % 2], second[(i + 1) % 2])

def find_nontrivial_fractions():
    fractions = []
    for first in range(11, 99):
        if first % 10 != 0:
            for second in range(first + 1, 100):
                temp = simplify_fraction_incorectly(first, second)
                if temp and temp[1] * first == temp[0] * second:
                    fractions.append((first, second))
    return fractions

def get_greatest_common_divisor(num1, num2):
    if num2 == 0:
        return num1
    return get_greatest_common_divisor(num2, num1 % num2)

def simplify_fraction_correctly(numerator, denominator):
    act1, act2, gcd = numerator, denominator, get_greatest_common_divisor(numerator, denominator)
    while gcd > 1:
        act1 /= gcd
        act2 /= gcd
        gcd = get_greatest_common_divisor(act1, act2)
    return (act1, act2)

def solve():
    fractions, numerator, denominator = find_nontrivial_fractions(), 1, 1
    for i in range(len(fractions)):
        numerator *= fractions[i][0]
        denominator *= fractions[i][1]
    return simplify_fraction_correctly(numerator, denominator)

if __name__ == '__main__':
    print(solve()[1])
