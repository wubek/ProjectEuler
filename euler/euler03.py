""" The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

def is_prime(number):
	counter = 2
	while counter**2 < number:
		if number % counter == 0:
			return False
		counter += 1
	return True

number = 600851475143
factor = 1
max = 1

while factor**2 < number:
	if number % factor == 0 and is_prime(factor):
		max = factor
	factor += 1

print(max)