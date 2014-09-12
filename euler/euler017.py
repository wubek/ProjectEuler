# author wukat
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
'''

def make_basic_dictionary():
    dictionary = {1: ("one", 3), 2: ("two", 3), 3: ("three", 5), 4: ("four", 4), 5: ("five", 4),
    6: ("six", 3), 7: ("seven", 5), 8: ("eight", 5), 9: ("nine", 4), 10: ("ten", 3), 11: ("eleven", 6),
    12: ("twelve", 6), 13: ("thirteen", 8), 15: ("fifteen", 7), 18: ("eighteen", 8), 
    20: ("twenty", 6), 30: ("thirty", 6), 40: ("forty", 5), 50: ("fifty", 5), 80: ("eighty", 6),
    100: ("hundred", 7), 1000: ("thousand", 8)}
    return dictionary

def reduce_tuples(tuples_sum):
    ''' First element in concatened tuples was string, second number, return tuple with sum of its
    like ("a", 1, "b", 2) => ("ab", 3)
    '''
    result = ["", 0]
    for i in range(len(tuples_sum)):
        result[i % 2] += tuples_sum[i]
    return tuple(result)

def translate_100_and_1000(which, number, dictionary):
    assert which == 100 or which == 1000
    if number % which > 0:
        return reduce_tuples(dictionary[number // which] + (" ", 0) + dictionary[which] + (" and ", 3) + translate_number(number % which, dictionary))
    else:
        return reduce_tuples(dictionary[number // which] + (" ", 0) + dictionary[which])

def translate_two_digits(number, dictionary):
    if number < 20:
        return reduce_tuples(dictionary[number % 10] + ("teen", 4))
    else:
        tens = (number // 10) * 10
        if number % 10 == 0:
            if tens in dictionary:
                return dictionary[tens]
            else:
                return reduce_tuples(dictionary[tens // 10] + ("ty", 2))
        else:
            if tens in dictionary:
                return reduce_tuples(dictionary[tens] + ("-", 0) + dictionary[number % 10])
            else:
                return reduce_tuples(dictionary[tens // 10] + ("ty-", 2) + dictionary[number % 10])


def translate_number(number, dictionary):
    if number >= 1000 and number < 10000:
        return translate_100_and_1000(1000, number, dictionary)
    elif number >= 100 and number < 1000:
        return translate_100_and_1000(100, number, dictionary)
    elif number in dictionary:
        return dictionary[number]
    else:
        return translate_two_digits(number, dictionary)


# not optimal, just summing up every instead of summing for example 1-99 and then use this sum to calculate 101-199
# and so on
def count_letters_from_1_to_number(to_num):
    sum_of_letters, dictionary = 0, make_basic_dictionary()
    for i in range(1, to_num + 1):
        temp = translate_number(i, dictionary)
        sum_of_letters += temp[1]
    return sum_of_letters


if __name__ == "__main__":
    print(count_letters_from_1_to_number(1000))