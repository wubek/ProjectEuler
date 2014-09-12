# author wukat
'''
Starting with the number 1 and moving to the right in a clockwise 
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 
spiral formed in the same way?
'''

def generate_spiral_diagonals(size):
    '''
    actual value (1, 2, ...); step - how many new elements insert in direction;
     direction - 0 is right, 1 is down, etc
    we can see that after every two directions step increases (+1)
    we can also see that moving right element on diagonal is the one before last 
    in this direction, and moving other directions
    is last
    '''
    assert size % 2 != 0 # it works on odd size of square
    act, step, direction = 1, 1, 0 
    yield act
    while act < size ** 2:
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
    print(sum(generate_spiral_diagonals(1001)))