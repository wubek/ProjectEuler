# author wukat
'''
All square roots are periodic when written as continued 
fractions and can be written in the form:

See details on problem web page.

It can be seen that the sequence is repeating. 
For conciseness, we use the notation sqrt23 = [4;(1,3,1,8)], 
to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations 
of (irrational) square roots are:

sqrt2=[1;(2)], period=1
sqrt3=[1;(1,2)], period=2
sqrt5=[2;(4)], period=1
sqrt6=[2;(2,4)], period=2
sqrt7=[2;(1,1,1,4)], period=4
sqrt8=[2;(1,4)], period=2
sqrt10=[3;(6)], period=1
sqrt11=[3;(3,6)], period=2
sqrt12=[3;(2,6)], period=2
sqrt13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N <= 13, have an odd period.

How many continued fractions for N <= 10000 have an odd period?
'''
from math import floor

def find_first_occurance(el, lst):
    for i in range(len(lst)):
        if el == lst[i]:
            return i

# ugly variables
def make_computations(up, num, b):
    down = (num - b**2) / up
    a = (2 * b // down if b >= down else 1)

    new_b = a * down - b
    if new_b ** 2 >= num:
        a = 0
        new_b = -b
    return a, down, new_b

def get_period(num):
    a = floor(num ** (1/2.0))
    up, b = 1, a
    past_tuples_set, past_tuples_list = set(), []
    while True:
        a, up, b = make_computations(up, num, b)
        if (a, up, b) in past_tuples_set:
            return len(past_tuples_list) - find_first_occurance((a, up, b), past_tuples_list)
        past_tuples_set.add((a, up, b))
        past_tuples_list.append((a, up, b))

def is_square(num):
    h = num & 0xF
    if h > 9:
        return False
    if h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8:
        return not num % round(num ** (1/2.0)) ** 2
    return False

def solve(limit):
    count = 1
    for i in range(3, limit + 1):
        if not is_square(i):
            temp = get_period(i)
            if temp and temp % 2:
                count += 1
    return count

if __name__ == '__main__':
    print(solve(10000))