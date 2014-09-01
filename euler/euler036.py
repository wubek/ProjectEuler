# author wukat
'''
The decimal number, 585 = 1001001001 2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_str_palindrom(str_number):
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-i - 1]:
            return False
    return True

def get_binary_string(number):
    binary_str = ""
    while number > 0:
        binary_str = str(number % 2) + binary_str
        number //= 2
    return binary_str

def solve(n):
    sum_of_palindroms = 0
    for i in range(1, n):
        if is_str_palindrom(str(i)) and is_str_palindrom(get_binary_string(i)):
            sum_of_palindroms += i
    return sum_of_palindroms


if __name__ == '__main__':
    print(solve(1000000))