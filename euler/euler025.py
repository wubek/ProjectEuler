# author wukat
'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''

def fib_gen():
    prev2, prev = 0, 1
    yield prev
    while True:
        prev2 = prev + prev2
        prev, prev2 = prev2, prev
        yield prev

def get_num_of_digits(number):
    return len(str(number))


if __name__ == '__main__':
    count = 0
    for i in fib_gen():
        count += 1
        if get_num_of_digits(i) >= 1000:
            print(count)
            break