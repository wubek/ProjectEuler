# author wukat
'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can L2 be made using any number of coins?
'''

# it's not good, created values should be stored (dict of lists of lists) and then used again 
# but it's good enought for this problem, so let leave it 
def generate_possibilities(coins_values, coins_amount, value):
    if value == 0:
        yield [0 for i in range(len(coins_values))]
    else:
        while coins_amount:
            actual_coin = coins_amount
            if value >= coins_values[actual_coin]:
                for i in range(value // coins_values[actual_coin], 0, -1):
                    actual_value = value - i * coins_values[actual_coin]
                    temp = generate_possibilities(coins_values, coins_amount - 1, actual_value)
                    for el in temp:
                        el[actual_coin] += i
                        yield el
            coins_amount -= 1
        temp = [0 for i in range(len(coins_values))]
        temp[0] = value
        yield temp


if __name__ == '__main__':
    coins_values = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50, 6: 100, 7: 200}
    count = 0
    for pos in generate_possibilities(coins_values, 7, 200):
        count += 1
    print(count)