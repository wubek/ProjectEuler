"""The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 ->  5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""

import datetime

def collatz_transform(number):
    if number % 2 == 0:
        return number/2
    else:
        return 3*number+1

def collatz_sequence_iter(start_number):
    lst = [start_number]
    while lst[-1] != 1:
        lst.append(collatz_transform(lst[-1]))
    return lst
    
def collatz_sequence_lst(start_number):
    return [x for x in collatz_generator(start_number)]

#courtesy of Wojtek Kasperek @ github.com/wukat
def collatz_generator(st):
    yield st
    while st > 1:
        st = collatz_transform(st)
        yield st
# ------------------ #

def max_collatz_chain_brute_force(number):
    max = 0
    start = 0
    for i in range(number, 1, -1):
        if max < len(collatz_sequence_lst(i)):
            max = len(collatz_sequence_lst(i))
            start = i
    return [max, start]

    
def max_collatz_chain_smarter(number):
    max_chain = 0
    max_chain_start_pos = 0
    known = {}
    for i in range(1, number+1):
        tmp = i
        distance = 0
        while tmp > 1:
            if tmp in known:
                distance += known[tmp]
                tmp = 1
            else:
                distance += 1
                tmp = tmp // 2 if tmp % 2 == 0 else 3*tmp+1
                
        known[i] = distance
        if max_chain < distance:
            max_chain = distance + 1 # ?
            max_chain_start_pos = i
    return [max_chain, max_chain_start_pos]
    
task = 1000000
        

time = datetime.datetime.now()
print("Smart v1 output:", max_collatz_chain_smarter(task))
time = datetime.datetime.now() - time
print("Time:", time)

time = datetime.datetime.now()
print("Brute output:", max_collatz_chain_brute_force(task))
time = datetime.datetime.now() - time
print("Time:", time)
