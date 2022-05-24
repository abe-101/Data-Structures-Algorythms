#!/usr/bin/python3
"""
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.
"""

def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)

def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1

    return count

assert(anagrams('restful', 'fluster') == True)
assert(anagrams('cats', 'tocs') == False)
assert(anagrams('monkeyswrite', 'newyorktimes') == True)
assert(anagrams('paper', 'reapa') == False)
assert(anagrams('elbow', 'below') == True)
assert(anagrams('tax', 'taxi') == False)
assert(anagrams('taxi', 'tax') == False)
assert(anagrams('night', 'thing') == True)
print('--Yay all tests passed!')
