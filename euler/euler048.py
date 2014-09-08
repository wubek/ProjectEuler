# author wukat
'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def power_only_last_n_digits(base, exponent, n = 10):
    div = 10 ** n
    if exponent == 1:
        return base % div
    return power_only_last_n_digits((base ** 2) % div, exponent // 2) * (base if exponent % 2 == 1 else 1)

def solve(n, numTo):
    sum_of_nums = 0
    for i in range(1, numTo + 1):
        sum_of_nums += power_only_last_n_digits(i, i)
    return sum_of_nums % 10 ** n


if __name__ == '__main__':
    print(solve(10, 1000))