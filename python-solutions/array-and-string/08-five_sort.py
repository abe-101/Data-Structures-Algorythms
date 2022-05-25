#!/usr/bin/python3
"""
five sort

Write a function, five_sort, that takes in a list of numbers as an argument. The function should rearrange elements of the list such that all 5s appear at the end. Your function should perform this operation in-place by mutating the original list. The function should return the list.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.
"""

def five_sort(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[j] == 5:
            j -= 1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        else:
            i += 1
    return nums



assert(five_sort([12, 5, 1, 5, 12, 7]) == [12, 7, 1, 12, 5, 5])
assert(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]) == [2, 2, 10, 6, 1, 5, 5, 5, 5, 5])
assert(five_sort([5, 5, 5, 1, 1, 1, 4]) == [4, 1, 1, 1, 5, 5, 5])
assert(five_sort([5, 5, 6, 5, 5, 5, 5]) == [6, 5, 5, 5, 5, 5, 5])
assert(five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5]) == [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5])

print('--Yay all tests passed!')
