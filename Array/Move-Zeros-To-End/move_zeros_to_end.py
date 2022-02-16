#!/usr/bin/python3

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    cnt = nums.count(0)
    
    while 0 in nums:
        nums.remove(0)
        
    for i in range(cnt):
        nums.append(0)

