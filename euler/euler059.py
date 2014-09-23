# author wukat
'''
Each character on a computer is assigned a unique code 
and the preferred standard is ASCII (American Standard 
Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, 
convert the bytes to ASCII, then XOR each byte with 
a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption 
key on the cipher text, restores the plain text; 
for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length 
as the plain text message, and the key is made 
up of random bytes. The user would keep the encrypted 
message and the encryption key in different locations, 
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, 
so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, 
the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long 
password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists 
of three lower case characters. Using cipher.txt (right 
click and 'Save Link/Target As...'), a file containing 
the encrypted ASCII codes, and the knowledge that the 
plain text must contain common English words, decrypt 
the message and find the sum of the ASCII values in the original text.
'''

from itertools import permutations

def gen_keys():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(alphabet) - 2):
        for j in range(i + 1, len(alphabet) - 1):
            for k in range(j + 1, len(alphabet)):
                for a, b, c in permutations([i, j, k]):
                    yield ord(alphabet[a]), ord(alphabet[b]), ord(alphabet[c])

def decrypt(text, key, key_len):
    letters_list = text.split(",")
    for i in range(len(letters_list)):
        letters_list[i] = int(letters_list[i]) ^ key[i % key_len]
    return letters_list

def to_string(decrypted_list):
    return "".join(map(chr, decrypted_list))

def test_if_correct(decrypted_text):
    if "the" in decrypted_text and "and" in decrypted_text and "all" in decrypted_text:
        return True

def solve(filename):
    with open(filename, "r") as input_text:
        for line in input_text:
            line = line[:-1]
            for key in gen_keys():
                decrypted_text = to_string(decrypt(line, key, len(key)))
                if test_if_correct(decrypted_text):
                    print(decrypted_text)
                    return sum(map(ord, decrypted_text))

if __name__ == '__main__':
    print(solve("euler059.input"))
