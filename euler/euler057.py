# author wukat
'''
It is possible to show that the square root 
of two can be expressed as an infinite continued fraction.

sqrt 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, 
but the eighth expansion, 1393/985, is the first example 
where the number of digits in the numerator exceeds 
the number of digits in the denominator.

In the first one-thousand expansions, how many fractions 
contain a numerator with more digits than denominator?
'''

def gen_expansions(n):
    below, up = 2, 1
    while n - 1:
        below, up = 2 * below + up, below
        n -= 1
        yield up, below

def get_frac(up, below):
    return up + below, below

def check_frac(up, below):
    up, below = get_frac(up, below)
    if len(str(up)) > len(str(below)):
        return 1
    return 0

if __name__ == '__main__':
    count = 0
    for up, below in gen_expansions(1000):
        count += check_frac(up, below)
    print(count)

