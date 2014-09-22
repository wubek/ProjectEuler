# author wukat
'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what 
is the maximum digital sum?
'''

def sum_of_digits(num):
	return sum(map(lambda dig: ord(dig) - ord("0"), str(num)))

if __name__ == '__main__':
	max_so_far = 0
	for a in range(1, 100):
		for b in range(1, 100):
			temp = sum_of_digits(a ** b)
			if temp > max_so_far:
				max_so_far = temp
	print(max_so_far)