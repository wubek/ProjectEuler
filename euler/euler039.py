# author wukat
'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

from math import floor

def find_all_triples(maxSumOfNumbers, dictionary):
    for i in range(1, int(maxSumOfNumbers/3)):
        for j in range(i + 1, int(2*maxSumOfNumbers/3)):
            k = (i**2 + j**2) ** 0.5
            if k - floor(k) == 0 and (int(k) + i + j) in dictionary:
                dictionary[int(k) + i + j] += 1

def solve():
    dictionary, p, max_so_far = {}, 0, 0
    for i in range(6, 1001):
        dictionary[i] = 0
    find_all_triples(1000, dictionary)
    for item in dictionary.items():
        if item[1] > max_so_far:
            max_so_far, p = item[1], item[0]
    return (max_so_far, p)

if __name__ == '__main__':
    print(solve())