""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million. """
from math import sqrt
import datetime

# Description of the algorithm available at
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
def eratosthenes_sieve(limit):
	sieve = [True for i in range(0,limit+1)]
	sieve[0] = False
	sieve[1] = False
	for i in range(2, int(sqrt(limit+1))+1):
		if sieve[i] == True:
			for j in range(i**2, limit+1, i):
				sieve[j] = False
	return sieve
	
def bool_to_int_lst(lst):
	return [x for x in range(0,len(lst)) if lst[x] == True]
	
def is_prime(number):
	counter = 2
	if number < 2:
		return False
	while counter**2 <= number:
		if number % counter == 0:
			return False
		counter += 1
	return True

def naive_prime_search(limit):
	return [x for x in range(2,limit+1) if is_prime(x)]

	
task = 2000000

print("Given number:", task)

print("Naive: ")
time = datetime.datetime.now()
print("Output:", sum(naive_prime_search(task)))
time = datetime.datetime.now() - time
print("Time:", time)

print("Eratosthenes sieve: ")
time = datetime.datetime.now()
print("Output:", sum(bool_to_int_lst(eratosthenes_sieve(task))))
time = datetime.datetime.now() - time
print("Time:", time)


