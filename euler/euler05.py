""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import datetime

def is_divisible(number, limit):
	for i in range(1,limit+1):
		if number % i != 0:
			return False
	return True

def is_divisible_lst(number, lst):
    for i in lst:
		if number % i != 0:
			return False
	return True
	
def smallest_product_brute(start, step, divMax):
	test = start
	while True:
		if is_divisible(test, divMax):
			return test
		test += step
		
def smallest_product_brute_lst(start, step, lst):
	test = start
	while True:
		if is_divisible_lst(test, lst):
			return test
		test += step

#not mine implementation
def SmallestProduct(divMax):
	num=1
	div=1
	add=0
	while div<=divMax:
		if num%div==0:
			div+=1
			add=num
		else:
			num+=add
	return num
# ------------------

def is_prime(number):
	counter = 2
	while counter**2 <= number:
		if number % counter == 0:
			return False
		counter += 1
	return True

def get_base_number(number):
	counter = 1
	for i in range(1,number+1):
		if is_prime(i):
			counter *= i
	return counter

def smallest_product_smarter_brute(divMax):
	base = get_base_number(divMax)
	return smallest_product_brute(base, 1, divMax)
	
def second_smarter_brute(divMax):
	base = get_base_number(divMax)
	return smallest_product_brute(base, 2520, divMax)

def third_smarter_brute(divMax):
	base = get_base_number(divMax)
	lst = []
	for i in range(1, divMax+1):
		if not is_prime(i):
			lst.append(i)
	base = smallest_product_brute_lst(base, 1, lst)
	return smallest_product_brute(base, 2520, divMax)
	
div = 20

start = datetime.datetime.now()
outcome = smallest_product_brute(1,1,div)
timer = datetime.datetime.now() - start
print("Brute:", outcome, timer)

start = datetime.datetime.now()
outcome = SmallestProduct(div)
timer = datetime.datetime.now() - start
print("SmallestProduct:", outcome, timer)

start = datetime.datetime.now()
outcome = smallest_product_smarter_brute(div)
timer = datetime.datetime.now() - start
print("smallest_product_smarter_brute:", outcome, timer)


start = datetime.datetime.now()
outcome = second_smarter_brute(div)
timer = datetime.datetime.now() - start
print("2nd_smallest_product_smarter_brute:", outcome, timer)

start = datetime.datetime.now()
outcome = third_smarter_brute(div)
timer = datetime.datetime.now() - start
print("3rd_smallest_product_smarter_brute:", outcome, timer)