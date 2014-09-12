# author wukat
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
and 5, giving the pandigital, 918273645, which is the concatenated product 
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
from euler032 import is_pandigital_str

def solve():
    max_so_far, number, num = "", 0, 1
    while num < 10000:
        i, concatenated = 1, ""
        while len(concatenated) < 9:
            concatenated += str(i * num)
            i += 1
        if len(concatenated) == 9:
            if is_pandigital_str(concatenated, 9):
                if concatenated > max_so_far:
                    max_so_far = concatenated
                    number = num
        num += 1
    return max_so_far



if __name__ == '__main__':
    print(solve())