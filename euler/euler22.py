# author wukat
'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(data):
    return merge(merge_sort(data[:(len(data) // 2)]), merge_sort(data[(len(data) // 2):])) if len(data) > 1 else data

def get_points_for_uppercase_word(word):
    return sum(map(lambda letter: ord(letter) - ord("A") + 1, word))

def get_points_for_ordered_words(words):
    points = 0
    for i in range(len(words)):
        points += (i + 1) * get_points_for_uppercase_word(words[i])
    return points


if __name__ == "__main__":
    with open("euler22.input", "r") as input_data:
        data = list(map(lambda name: name.replace("\"",""), input_data.read().split(",")))
    data = merge_sort(data) # data.sort() is faster
    print(get_points_for_ordered_words(data))

