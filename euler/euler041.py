# author wukat
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from euler005 import is_prime
from euler024 import generate_parmutations_recursive

def make_num(lst):
    num = 0
    for i in range(len(lst) - 1, -1, -1):
        num += lst[i] * (10 ** (len(lst) - i - 1))
    return num

def solve():
    for j in range(9, 0, -1):
        for i in generate_parmutations_recursive([], [i for i in range(j, 0, -1)]):
            i = make_num(i)
            if is_prime(i):
                return i

if __name__ == '__main__':
    print(solve())