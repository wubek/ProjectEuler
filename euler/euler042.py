# author wukat
'''
The nth term of the sequence of triangle numbers is given by, tn = 1/2 n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

def gen_set_of_first_n_triangle_nums(n):
    res = set()
    for i in range(1, n + 1):
        res.add(0.5 * i * (i + 1))
    return res

def get_letter_number(letter):
    return ord(letter) - ord('A') + 1

def check_word(word, triangles):
    return True if sum(map(get_letter_number, word)) in triangles else False

def solve(fileName):
    count, triangles = 0, gen_set_of_first_n_triangle_nums(27)
    with open(fileName, "r") as inputWords:
        words = inputWords.read()
        for word in words.replace("\"", "").split(","):
            if check_word(word, triangles):
                count += 1
    return count


if __name__ == '__main__':
    print(solve("euler042.input"))