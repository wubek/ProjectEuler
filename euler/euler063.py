# author wukat
'''
The 5-digit number, 16807=7^5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

def len_of_num(num):
    return len(str(num))

def solve():
    count = 0
    for i in range(2, 10): # it's easy to see that only 1-digit numbers can create it
        power= 1
        while True:
            length = len_of_num(i ** power) 
            if length == power:
                count += 1
            elif length < power:
                break
            power += 1
    return count + 1 # because 1 ^ 1 is also ok

if __name__ == '__main__':
    print(solve())