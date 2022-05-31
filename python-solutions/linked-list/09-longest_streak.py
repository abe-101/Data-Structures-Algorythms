#!/usr/bin/python3
"""
Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest
consecutive streak of the same value within the list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def longest_streak(head):
    # Time: O(n)
    # Space: O(1)
    current = head
    max_streak = 0 
    current_streak = 0
    prev_value = None
    while current is not None:
        if current.val == prev_value:
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)
        prev_value = current.val
        current = current.next
    return max_streak


a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 5 -> 5 -> 7 -> 7 -> 7 -> 6
assert(longest_streak(a) == 3)
# test_01:
a = Node(3)
b = Node(3)
c = Node(3)
d = Node(3)
e = Node(9)
f = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 3 -> 3 -> 3 -> 3 -> 9 -> 9
assert(longest_streak(a) == 4)
# test_02:
a = Node(9)
b = Node(9)
c = Node(1)
d = Node(9)
e = Node(9)
f = Node(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# 9 -> 9 -> 1 -> 9 -> 9 -> 9
assert(longest_streak(a) == 3)
# test_03:
a = Node(5)
b = Node(5)
a.next = b
# 5 -> 5
assert(longest_streak(a) == 2)
# test_04:
a = Node(4)
# 4
assert(longest_streak(a) == 1)
# test_05:
assert(longest_streak(None) == 0)
print('-- Yay test completed!')
