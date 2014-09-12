"""A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def is_palindrome(number):
    txt = str(number)
    for i in range(0,(len(txt)//2)):
        j = len(txt)-i-1
        if txt[i] != txt[j]:
            return False
    return True
    
def find_palindromes(limit):
    lst = []
    for i in range(limit,0,-1):
        for j in range(limit, 0, -1):
            if is_palindrome(i*j):
                lst.append(i*j)
    return lst

    
print(max(find_palindromes(999)))

