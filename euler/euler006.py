"""The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
"""

def sum_of_squares(number):
    sum_of_squares = 0
    for i in range(1,number+1):
        sum_of_squares += i**2
    return sum_of_squares
    
def square_of_sum(number):
    square_of_sum = sum(range(1,number+1))
    return square_of_sum**2

task = 100
print(abs(sum_of_squares(task)-square_of_sum(task)))