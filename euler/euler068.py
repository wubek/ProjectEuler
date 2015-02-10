# author wukat
'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line 
adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external 
node (4,3,2 in this example), each solution can be described uniquely. For example, the above 
solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are 
eight solutions in total.

Total   Solution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3
10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5
11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6
12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string 
for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- 
and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
'''

import itertools 

def make_ring(size, possible_numbers):
    ring = [[0, 0, 0] for i in range(0,size)]
    results = []
    for i in range(9, 50):
        for result in solve_with_sum(i, possible_numbers, ring):
            results.append(result)
    print(max(results))

def gen_three_to_sum(suma, possible_numbers):
    for i in range(len(possible_numbers) - 2):
        for j in range(i + 1, len(possible_numbers) - 1):
            for k in range(j + 1, len(possible_numbers)):
                if possible_numbers[i] + possible_numbers[j] + possible_numbers[k] == suma:
                    for permutations in itertools.permutations([possible_numbers[i], possible_numbers[j], possible_numbers[k]]):
                        yield permutations

def gen_two_to_sum(suma, possible_numbers):
    for i in range(len(possible_numbers) - 1):
        for j in range(i + 1, len(possible_numbers)):
            if possible_numbers[i] + possible_numbers[j] == suma:
                yield [possible_numbers[i], possible_numbers[j]]
                yield [possible_numbers[j], possible_numbers[i]]

def solve_with_sum(suma, possible_numbers, ring):
    for beginning in gen_three_to_sum(suma, possible_numbers):
        ring[0][0] = beginning[0]
        ring[0][1] = beginning[1]
        ring[0][2] = beginning[2]
        ring[1][1] = ring[0][2]
        ring[len(ring) - 1][2] = ring[0][1]
        for result in go_on(ring, list(set(possible_numbers).difference(set(beginning))), suma, 1):
            yield result

def go_on(ring, possible_numbers, suma, index):
    if index == len(ring) - 1:
        if sum(ring[index]) + possible_numbers[0] == suma:
            yield make_result_string(ring, possible_numbers[0])
    else:
        sumaTemp = suma - ring[index][1]
        for pair in gen_two_to_sum(sumaTemp, possible_numbers):
            ring[index][0] = pair[0]
            ring[index][2] = pair[1]
            ring[index + 1][1] = pair[1]
            for result in go_on(ring, list(set(possible_numbers).difference(set(pair))), suma, index + 1):
                yield result

def make_result_string(ring, number):
    strings = ["" for i in range(len(ring))]
    for i in range(len(ring) - 1):
        strings[i] = int(str(ring[i][0]) + str(ring[i][1]) + str(ring[i][2]))
    strings[len(ring) - 1] = int(str(number) + str(ring[len(ring) - 1][1]) + str(ring[len(ring) - 1][2]))
    if min(strings) == strings[0]:
        result = ''.join(map(str, strings))
        if len(result) == 16:
            return result

if __name__ == "__main__":
    make_ring(5, [1,2,3,4,5,6,7,8,9,10])

