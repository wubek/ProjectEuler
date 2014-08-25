"""Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
#author: wubek
#I don't like how this problem is formulated, as I have no way to know where these numbers end...

def sum_digit_power(number, power):
	my_sum = 0
	txt = str(number)
	for digit in txt:
		my_sum += int(digit)**power
	return my_sum

if __name__ == "__main__":
	lst = []
	power = 5
	for i in range(2,500000): #completely arbitrary, hail magic numbers!
		if sum_digit_power(i, power) == i:
			lst.append(i)
	print(lst)
	print("Answer:",sum(lst))