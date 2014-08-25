# author wukat
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

def get_sum_of_div(number):
    sum_of_div = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum_of_div += i
            if i ** 2 != number:
                sum_of_div += number // i
    return sum_of_div

def make_sum_of_div_dict(from_num, to_num):
    dictionary = {}
    for i in range(from_num, to_num + 1):
        dictionary[i] = get_sum_of_div(i)
    return dictionary

def check_if_abundant(dictionary_num_sum_of_div, number):
    if number in dictionary_num_sum_of_div:
        return True if dictionary_num_sum_of_div[number] > number else False
    else:
        temp = get_sum_of_div(number)
        dictionary_num_sum_of_div[number] = temp
        return True if temp > number else False

def create_abundants_list(from_num, to_num, dictionary_num_sum_of_div):
    abundants = []
    for i in range(from_num, to_num + 1):
        if check_if_abundant(dictionary_num_sum_of_div, i):
            abundants.append(i)
    return abundants

def create_all_that_can_be_repr_as_sum_of_2_abundants_set(abundants):
    all_that_can_be_repr_as_sum_of_2_abundants = set()
    while abundants:
        abundant = abundants.pop()
        all_that_can_be_repr_as_sum_of_2_abundants.add(2 * abundant)
        for second_abundant in abundants:
            all_that_can_be_repr_as_sum_of_2_abundants.add(abundant + second_abundant)
    return all_that_can_be_repr_as_sum_of_2_abundants

if __name__ == '__main__':
    all_numbers_to_consider = set(i for i in range(1, 28124))
    abundants = create_abundants_list(12, 28112, make_sum_of_div_dict(12, 28112))
    all_that_can_be_repr_as_sum_of_2_abundants = create_all_that_can_be_repr_as_sum_of_2_abundants_set(abundants)
    print(sum(all_numbers_to_consider - all_that_can_be_repr_as_sum_of_2_abundants))




