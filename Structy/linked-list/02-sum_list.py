#!/usr/bin/python3
"""
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def sum_list(head):
    # Time: O(n) n is the number of nodes
    # Space: O(1)
    list_sum = 0
    current = head
    while current is not None:
        list_sum += current.val
        current = current.next
    return list_sum


# Recursive
def sum_list(head):
    # Time: O(n) n is the number of nodes
    # Space: O(n)
    if head is None:
        return 0
    return head.val + sum_list(head.next)

# test_00:
a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)
a.next = b
b.next = c
c.next = d
d.next = e
# 2 -> 8 -> 3 -> -1 -> 7
assert(sum_list(a) == 19)
# test_01:
x = Node(38)
y = Node(4)
x.next = y
# 38 -> 4
assert(sum_list(x) == 42)
# test_02:
z = Node(100)
# 100
assert(sum_list(z) == 100)
# test_03:
assert(sum_list(None) == 0)
print('-- Yay test completed!')
