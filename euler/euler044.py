# author wukat
'''
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. 
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their 
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their 
sum and difference are pentagonal and D = |Pk - Pj| is minimised; 
what is the value of D?
'''

from itertools import count
from math import sqrt, floor    

def gen_pantagonal(startFrom = 1):
    for i in count(startFrom):
        yield i * (3*i - 1) / 2

def test_pentagonal(numToTest):
    temp = (sqrt(24 * numToTest + 1) + 1) / 6
    return True if temp - floor(temp) == 0 else False

def solve():
    pentagonals = []
    for first in gen_pantagonal():
        for second in pentagonals:
            if (test_pentagonal(first + second)):
                if (test_pentagonal(first - second)):
                    return first - second
        pentagonals.append(first)

if __name__ == '__main__':
    print(solve())