# author wukat
'''
The square root of 2 can be written as an infinite continued fraction.

The infinite continued fraction can be written, sqrt2 = [1;(2)], 
(2) indicates that 2 repeats ad infinitum. In a similar way, 
sqrt23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued 
fractions for square roots provide the best rational approximations. 
Let us consider the convergents for sqrt2.

Hence the sequence of the first ten convergents for sqrt2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent 
of the continued fraction for e.
'''

def make_e_frac_list(limit):
    result = [2]
    count = 2
    for i in range(1, limit + 1):
        if i % 3 == 2:
            result.append(count)
            count += 2
        else:
            result.append(1)
    return result

def make_frac_from_list(frac_list):
    act = frac_list.pop()
    up = 1
    while frac_list:
        num = frac_list.pop()
        up_new = act
        act = num * act + up
        up = up_new
    return act, up

def sum_of_digits(num):
    return sum(map(lambda dig: ord(dig) - ord("0"), str(num)))

if __name__ == '__main__':
    print(sum_of_digits(make_frac_from_list(make_e_frac_list(99))[0]))