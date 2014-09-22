# author wukat
'''
Starting with 1 and spiralling anticlockwise 
in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along 
the bottom right diagonal, but what is more interesting 
is that 8 out of the 13 numbers lying along both diagonals 
are prime; that is, a ratio of 8/13 ~= 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. If this 
process is continued, what is the side length of the square 
spiral for which the ratio of primes along both diagonals 
first falls below 10%?
'''

from euler005 import is_prime

def generate_spiral_diagonals():
    '''
    actual value (1, 2, ...); 
    step - how many new elements insert in direction;
    direction - 0 is right, 1 is up, etc
    we can see that after every two directions step increases (+1)
    we can also see that moving right element on diagonal is the one before last 
    in this direction, and moving other directions is last
    '''
    act, step, direction = 1, 1, 0 
    yield act
    while True:
        for i in range(step):
            act += 1
            if direction == 0 and i == step - 2:
                yield act
            elif direction != 0 and i == step - 1:
                yield act
        direction += 1
        direction %= 4
        if direction % 2 == 0:
            step += 1

if __name__ == '__main__':
    count, primes_count = 0, 0
    for i in generate_spiral_diagonals():
        if is_prime(i):
            primes_count += 1
        count += 1
        if count % 4 == 1 and primes_count > 0:
            if primes_count * 10 < count:
                print(((count + 1) / 2))
                break