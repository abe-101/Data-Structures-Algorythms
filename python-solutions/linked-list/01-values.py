#!/usr/bin/python3
"""
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def linked_list_values(head):
    current = head
    values = []
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d
assert(linked_list_values(a) == [ 'a', 'b', 'c', 'd' ])

# test_01:
x = Node("x")
y = Node("y")
x.next = y
# x -> y
assert(linked_list_values(x) == [ 'x', 'y' ])

# test_02:
q = Node("q")
# q
assert(linked_list_values(q) == [ 'q' ])

# test_03:
assert(linked_list_values(None) == [ ])

print('-- Yay test completed!')
