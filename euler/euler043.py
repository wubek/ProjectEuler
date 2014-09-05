# author wukat
'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

from euler024 import generate_parmutations_recursive
from euler041 import make_num

def check_num(numList):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(len(divisors), 0, -1):
        if make_num(numList[i : (i + 3)]) % divisors.pop() != 0:
            return False
    return True

def solve():
    sum_of_nums = 0
    for num in generate_parmutations_recursive([], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]):
        if num[0] != 0:
            if check_num(num):
                sum_of_nums += make_num(num)
    return sum_of_nums

if __name__ == '__main__':
    print(solve())