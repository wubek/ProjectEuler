# author wukat
'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from euler005 import is_prime
from euler024 import generate_parmutations_recursive
from euler041 import make_num

def gen_sequences(set_of_nums, first_num):
    pass

def check_number(number):
    permutations = set()
    for num_list in generate_parmutations_recursive([], map(lambda x: ord(x) - ord("0"),str(number))):
        permutations.add(make_num(num_list))
    pass

if __name__ == '__main__':
    for i in range(1234, 3333):
        if is_prime(i):
            temp = check_number(i)
            if temp:
                print(temp)
            

