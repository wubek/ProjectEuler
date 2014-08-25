# author wukat
'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''


def generate_parmutations_recursive(so_far, rest):
    ''' Start with so_far = [] and rest = [sorted elements] to get ordered permutations generator '''
    if rest:
        for element in rest:
            for t in generate_parmutations_recursive(so_far + [element], [i for i in rest if i != element]):
                yield t
    else:
        yield so_far

if __name__ == '__main__':
    count = 0
    for i in generate_parmutations_recursive([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        count += 1
        if count == 1000000:
            result = ""
            for j in i:
                result += str(j)
            print(result)
            break