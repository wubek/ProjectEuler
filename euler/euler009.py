# author wukat
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_triples(sumOfNumbers):
    ''' Returns tuple (i, j, k) that i ** 2 + j ** 2 = k ** 2 
    and i + j + k = sumOfNumbers; (i < j < k)'''
    for i in range(1, int(sumOfNumbers/3)):
        for j in range(i + 1, int(2*sumOfNumbers/3)):
            k = (i**2 + j**2) ** 0.5
            if i + j + k == sumOfNumbers:
                return (i, j, int(k))

if __name__ == "__main__":
    found = find_triples(1000)
    result = 1
    for i in found:
        result *= i
    print(result)