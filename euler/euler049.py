# author wukat
'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from euler005 import is_prime
from euler041 import make_num

def generate_parmutations_recursive_better(so_far, rest):
    if rest:
        for i in range(len(rest)):
            element = rest[i]
            for t in generate_parmutations_recursive_better(so_far + [element], [rest[j] for j in range(len(rest)) if i != j]):
                yield t
    else:
        yield so_far

def check_number(number, used):
    permutations = set()
    for num_list in generate_parmutations_recursive_better([], map(lambda x: ord(x) - ord("0"), str(number))):
        permutations.add(make_num(num_list))
    used.update(permutations)
    
    list_of_permutations = list(permutations)
    list_of_permutations.sort()
    
    for i in range(len(list_of_permutations) - 2):
        first = list_of_permutations[i]
        if first > 1000 and is_prime(first):
            for j in range(i + 1, len(list_of_permutations) - 1):
                second = list_of_permutations[j]
                if is_prime(second):
                    for k in range(j + 1, len(list_of_permutations)):
                        third = list_of_permutations[k]
                        if is_prime(third):
                            if 2*second == first + third:
                                return (first, second, third)
        
def solve():
    used = set()
    for i in range(1234, 3333):
        if i not in used and is_prime(i):
            temp = check_number(i, used)
            if temp and temp != (1487, 4817, 8147):
                print(temp)

if __name__ == '__main__':
    solve()
    

