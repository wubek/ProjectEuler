# author wukat
'''
2 ^ 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ^ 1000?
'''

def to_digit(char):
    return ord(char) - ord("0")

def mul_str_number_and_2(str_number):
    result, transfer, string_repr = [], 0, ""
    for dig in reversed(str_number):
        temp = to_digit(dig) * 2 + transfer
        transfer = temp // 10
        result.append(str(temp % 10))

    if transfer > 0:
        for char in reversed(str(transfer)):
            result.append(char)

    for char in reversed(result):
        string_repr += char 

    return string_repr

def power_2_on_strings(exponent):
    act = "2"
    for i in range(exponent - 1):
        act = mul_str_number_and_2(act)
    return act

def add_digits_in_str_number(str_number):
    return sum(map(to_digit, str_number))

def add_digits_in_number(number):
    return sum(map(to_digit, str(number)))


if __name__ == "__main__":
    # Uses python property - having big range long numbers
    print(add_digits_in_number(2**1000))
    # Using stringss
    print(add_digits_in_str_number(power_2_on_strings(1000)))