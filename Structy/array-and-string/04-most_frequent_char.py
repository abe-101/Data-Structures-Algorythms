#!/usr/bin/python3
"""
most frequent char

Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""

def most_frequent_char(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    best = s[0]
    for char in s:
        if count[char] > count[best]:
            best = char
    return best

assert(most_frequent_char('bookeeper') == 'e')
assert(most_frequent_char('david') == 'd')
assert(most_frequent_char('abby') == 'b')
assert(most_frequent_char('mississippi') == 'i')
assert(most_frequent_char('potato') == 'o')
assert(most_frequent_char('eleventennine') == 'e')
assert(most_frequent_char('riverbed') == 'r')

print('--Yay all tests passed!')
