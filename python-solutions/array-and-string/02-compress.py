#!/usr/bin/python3
"""
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters.
"""

def compress(s):
    s += '!'
    i = j = 0
    result = []
    while j < len(s):
        if s[i] == s[j]:
            j += 1
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num))
                result.append(s[i])
            i = j

    return ''.join(result)

assert(compress('ccaaatsss') == '2c3at3s')
assert(compress('ssssbbz') == '4s2bz')
assert(compress('ppoppppp') == '2po5p')
assert(compress('nnneeeeeeeeeeeezz') == '3n12e2z')
assert(compress('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy') =='127y')

print('--Yay all tests passed!')
