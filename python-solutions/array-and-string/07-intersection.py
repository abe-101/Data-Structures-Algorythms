#!/usr/bin/python3
"""
intersection

Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""
def intersection(a, b):
    set_a = set(a)
    return [ item for item in b if item in set_a ]

assert(intersection([4,2,1,6], [3,6,9,2,10]) == [6,2])
assert(intersection([2,4,6], [4,2]) == [4,2])
assert(intersection([4,2,1], [1,2,4,6]) == [1,2,4])
assert(intersection([0,1,2], [10,11]) == [])
a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
assert(intersection(a, b) == [ i for i in range(0, 50000) ])

print('--Yay all tests passed!')
