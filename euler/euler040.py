# author wukat
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

from itertools import count

def gen_next_num_and_index():
    index = 1
    for i in count(1):
        temp = len(str(i))
        yield (i, index, temp)
        index += temp

def solve():
    acutal_index, product = 1, 1
    for item in gen_next_num_and_index():
        if item[1] <= acutal_index and item[1] + item[2] > acutal_index:
            product *= int(str(item[0])[acutal_index - item[1]])
            acutal_index *= 10
            if acutal_index > 1000000:
                break
    return product


if __name__ == '__main__':
    print(solve())