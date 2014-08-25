""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples(limit, numbers):
    lst = []
    for number in numbers:
        lst = find_multiples(limit, number, lst)
    return sum(lst)
    
def find_multiples(limit, num, lst):
    new_lst = lst
    i = 1
    while i*num < limit:
        if i*num not in new_lst:
            new_lst.append(i*num)
        i += 1
    return new_lst
    
x = sum_of_multiples(1000, [3,5])
print(x)