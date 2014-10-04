# author wukat
'''
The cube, 41063625 (345^3), can be permuted to produce 
two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly 
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations 
of its digits are cube.
'''

from itertools import permutations
from math import floor

# try other way round
def is_cube(num):
    temp = num ** (1 / 3.0)
    return not num - round(temp) ** 3

def has_five_cube_permutations(num):
    count, used = 0, set()
    for num in permutations(str(num)):
        if num not in used:
            if is_cube(int("".join(num))):
                count += 1
            used.add(num)
    if count == 5:
        return True

def solve():
    num = 350
    while not has_five_cube_permutations(num ** 3):
        num += 1
    return num

if __name__ == '__main__':
    print(solve())
