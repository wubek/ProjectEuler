"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?"""
#author: wubek

from euler005 import is_prime
from euler010 import eratosthenes_sieve
import datetime

def generate_circular(lst):
    yield(lst)
    for i in range(1,len(lst)):
        new_lst = ""
        for shift in range(0, len(lst)):
            new_lst += lst[(i+shift)%len(lst)]
        yield new_lst
 
def generate_circular_lst(lst):
    ret_lst = [lst]
    for i in range(1,len(lst)):
        new_lst = ""
        for shift in range(0, len(lst)):
            new_lst += lst[(i+shift)%len(lst)]
        ret_lst.append(new_lst)
    return ret_lst
     
def is_circular_prime(number):
    for rotation in number:
        if not is_prime(int(rotation)):
            return False
    return True
            
if __name__ == "__main__":
    task = 1000000
    checked = set()
    counter = 0
    """time = datetime.datetime.now()
    for number in range(3, task, 2):
        if number in checked:
            continue
        rotations = generate_circular_lst(str(number))
        checked |= set(rotations)
        if is_circular_prime(rotations):
            counter += 1
    time = datetime.datetime.now() - time
    print("Answer:",counter)
    print(">>", time)
    
    time = datetime.datetime.now()
    primes_bool = eratosthenes_sieve(task+1)
   
    for number in range(2,task+1):
        if not primes_bool[number]:
            continue
        if is_circular_prime(generate_circular_lst(str(number))):
            counter += 1
    time = datetime.datetime.now() - time
    print("Answer:",counter)
    print(">>", time)"""
    
    
  
            
  
