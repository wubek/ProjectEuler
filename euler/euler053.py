# author wukat
'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5 C 3 = 10.

In general,

n C r =	
n! / r! (n-r)!
,where r <= n, n! = n * (n-1) * ... *3*2*1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23 C 10 = 1144066.

How many, not necessarily distinct, values of  n C r, for 1 <= n <= 100, 
are greater than one-million?
'''

# we know that n C r = n C (n - r), so if n C r is greater than one-million, 
# then n - 2r + 1 numbers are greater than one-million

def factorial(n):
	assert n >= 0
	res, i = 1, 2
	for i in range(2, n + 1):
		res *= i
	return res

def newton(n, r):
	assert n >= 0 and r > 0 and r <= n
	up = 1
	for i in range(r):
		up *= n - i
	return up / factorial(r)

# values set stiff
def count_greater_than_million():
	count = 0
	for num in range(23, 101):
		for r in range(1, int(num // 2) + 1):
			if newton(num, r) > 1000000:
				count += num - 2 * r + 1
				break
	return count 

if __name__ == '__main__':
	print(count_greater_than_million())
