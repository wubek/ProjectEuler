# author wukat
'''
In England the currency is made up of pound, L, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, L1 (100p) and L2 (200p).
It is possible to make L2 in the following way:

1xL1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can L2 be made using any number of coins?
'''

def generate_possibilities(coins, value, used = 0):
    print(value, used)
    if value == 0:
        yield [0 for i in range(len(coins))]
    else:
        for which_coin in range(len(coins) - used - 1, -1, -1):
            #print(which_coin)
            actual_coin = coins[which_coin]
            if actual_coin > 1:
         #   print(actual_coin)
                #print([i for i in range(value // actual_coin, 0, -1)])
                for take_this_many_times in range(value // actual_coin, 0, -1):
                    if value - take_this_many_times*actual_coin > 0:
                        for temp in generate_possibilities(coins, value - take_this_many_times*actual_coin, used + 1):
                            list_of_coins_usage = [0 for i in range(len(coins))]
                            list_of_coins_usage[which_coin] = take_this_many_times
                            for i in range(len(temp)):
                                list_of_coins_usage[i] += temp[i]
                            yield list_of_coins_usage
                    else:
                        list_of_coins_usage = [0 for i in range(len(coins))]
                        list_of_coins_usage[which_coin] = take_this_many_times
                        yield list_of_coins_usage
            else:
                list_of_coins_usage = [0 for i in range(len(coins))]
                list_of_coins_usage[which_coin] = value
                yield list_of_coins_usage


if __name__ == '__main__':
    coins = {0: 1, 1: 2, 2: 5, 3: 10, 4: 20, 5: 50, 6: 100, 7: 200}
    res = set()
    for pos in generate_possibilities(coins, 10):
        res.add(tuple(pos))
        print(pos)
    print(len(res))