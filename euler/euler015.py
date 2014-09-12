# author wukat
'''
Starting in the top left corner of a 2x2 grid, and only being able 
to move to the right and down, there are exactly 6 routes 
to the bottom right corner.

https://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20x20 grid?
'''
import datetime

'''
Example:
3x3:
N N N
N N N
1 1 1

possible paths after computing:
6 3 1
3 2 1
1 1 1

4x4:
N N N N
N N N N
N N N N
1 1 1 1

after:
20 10  4  1
10  6  3  1
 4  3  2  1
 1  1  1  1

so possible paths amount is a sum of right and down elemnts 
(or one of them, if second doesn't exist).
'''

def make_init_possible_paths_amount(size):
    paths = []
    for i in range(1, size + 1):
        paths.append([None for j in range(i)])
    for i in range(size):
        paths[size - 1][i] = 1
    return paths

def count_paths_dynamic(size):
    size += 1
    paths = make_init_possible_paths_amount(size)
    for i in range(size - 2, -1, -1):
        paths[i][i] = 2 * paths[i + 1][i]
        for j in range(i - 1, -1, -1):
            paths[i][j] = paths[i + 1][j] + paths[i][j + 1]
    return paths[0][0]

if __name__ == "__main__":
    start = datetime.datetime.now()
    print(count_paths_dynamic(20))
    print(datetime.datetime.now() - start)