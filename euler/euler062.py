# author wukat
'''
The cube, 41063625 (345^3), can be permuted to produce 
two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly 
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations 
of its digits are cube.
'''

def make_special_num(num):
    list_of_digit_occurances, res = [0 for i in range(10)], ""
    for i in str(num):
        list_of_digit_occurances[int(i)] += 1
    for i in range(9, -1, -1):
        res += str(i) + str(list_of_digit_occurances[i])
    return res

def solve():
    dictionary_of_special, num = {}, 100
    while True:
        special = make_special_num(num ** 3)
        if special in dictionary_of_special:
            dictionary_of_special[special].append(num)
            if len(dictionary_of_special[special]) == 5:
                return dictionary_of_special[special][0] ** 3
        else:
            dictionary_of_special[special] = [num]
        num += 1

if __name__ == '__main__':
    print(solve())
