"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from math import ceil
import datetime
import operator

def create_div_dictionary(number):
	dict = {}
	for i in range(2,number+1):
		div_list = [1]
		for j in range(2, int(i**0.5)+1):
            if i % j == 0:
				div_list.append(j)
				tmp = i / j
				if tmp != j:
					div_list.append(int(tmp))
		dict[i] = div_list
	return dict

def print_dict(dict):
	for entry in dict:
		print(entry, ":", dict[entry])

def create_div_sum_dictionary(dict):
	new_dict = {}
	for entry in dict:
		new_dict[entry] = sum(dict[entry])
	return new_dict
		
def find_amicables(number):
	amicable = {}
	dict = create_div_dictionary(number)
	div_sum_dict = create_div_sum_dictionary(dict)
	
	for key in div_sum_dict:
		for ami_key in div_sum_dict:
			if key == div_sum_dict[ami_key] and ami_key == div_sum_dict[key] and key != ami_key:
				if key not in amicable.values():
					amicable[key] = ami_key
	return amicable


task = 10000

time = datetime.datetime.now()
amicables = find_amicables(task)
print("Sum of amicable numbers:", sum(amicables)+sum(amicables.values()))
time = datetime.datetime.now() - time
print("Time:", time)
print("Amicable numbers found:")
print_dict(amicables)


