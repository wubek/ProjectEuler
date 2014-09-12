# author wukat
'''
A unit fraction contains 1 in the numerator. The decimal 
representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.
'''

def get_decimal_part_cycle_len_1_over_number(number):
    ''' 1/number = 0.decimal_part '''
    rests = [10]
    while rests[-1] % number != 0:
        rest = (rests[-1] % number) * 10
        for i in range(len(rests)):
            if rest == rests[i]:
                return len(rests) - i
        rests.append(rest)
    return 0 

def find_denominator_with_longest_decimal_cycle(from_num, to_num):
    max_so_far, div = 0, None
    for i in range(from_num, to_num):
        temp = get_decimal_part_cycle_len_1_over_number(i)
        (max_so_far, div) = (temp, i) if temp > max_so_far else (max_so_far, div)
    return div

if __name__ == '__main__':
    print(find_denominator_with_longest_decimal_cycle(1, 1000))