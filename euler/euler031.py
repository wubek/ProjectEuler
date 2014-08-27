# author wukat
'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can L2 be made using any number of coins?
'''

def generate_possibilities(coins, value, list_of_coins_usage2, act = 0):
    print(value, list_of_coins_usage2, act)
    list_of_coins_usage = []
    for i in list_of_coins_usage2:
        list_of_coins_usage.append(i)
    if value == 0:
        yield list_of_coins_usage

    for i in range(1, len(coins) - act):
        actual_coin = coins[len(coins) - i - 1]
        for j in range(value // actual_coin, 0, -1):
            list_of_coins_usage[len(coins) - i - 1] += j
            for pos in generate_possibilities(coins, value - j *  actual_coin, list_of_coins_usage, act + 1):
                yield pos

if __name__ == '__main__':
    coins = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50, 6: 100, 7: 200}
    print(set({1: "d"}))
    for pos in generate_possibilities(coins, 10, [0, 0, 0, 0, 0, 0, 0]):
        print(pos)