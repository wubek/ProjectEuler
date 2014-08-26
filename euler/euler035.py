"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?"""
#author: wubek
"""197
971
719"""

from euler005 import is_prime

def construct_circular(number):
    lst = [number]
    conv = str(number)
    for shift in range(1, len(conv)):
       lst.append(int([conv[(x+shift)%len(conv)] for x in conv))
    print(lst)
        

if __name__ == "__main__":
    construct_circular(10)