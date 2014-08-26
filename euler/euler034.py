"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included."""
#author: wubek

def factorial(number):
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    return factorial

def find_digit_factorial(number):
    lst = set()
    for i in range(3, number+1):
        conv = str(i)
        msum = 0
        for digit in conv:
            msum += factorial(int(digit))
        if msum == i:
            lst.add(i)
      #  if i > len(conv)*factorial(9):
      #      break
    return lst
    
if __name__ == "__main__":
    print("Answer:", sum(find_digit_factorial(999999)))

"""
When to stop iterating? Need to explore this 
99 725760
999 1088640
9999 1451520
99999 1814400
999999 < 2177280
9999999 > 2540160
[max number composed from n digits] >< sum of factorized digits """