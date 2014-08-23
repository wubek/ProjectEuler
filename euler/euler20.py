"""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
def factorial(number):
	starter = 1
	for i in range(2,number+1):
        starter *= i
	return starter

def sum_of_digits(number):
	lst = str(number)
	msum = 0
	for i in lst:
		msum += int(i)
	return msum
	
print(factorial(100))
print(sum_of_digits(factorial(100)))