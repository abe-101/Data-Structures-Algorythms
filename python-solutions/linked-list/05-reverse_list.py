#!/usr/bin/python3
"""
Write a function, reverse_list, that takes in the head of a linked list
as an argument. The function should reverse the order of the nodes in the 
linked list in-place and return the new head of the reversed linked list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def reverse_list(head):
    # Time: O(n)
    # Space: O(1)
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# Recursive
def reverse_list(head, prev = None):
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)


# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f
assert(reverse_list(a) == f)
# test_01:
x = Node("x")
y = Node("y")
x.next = y
# x -> y
assert(reverse_list(x) == y) # y -> x
# test_02:
p = Node("p")
# p
assert(reverse_list(p) == p)# p
print('-- Yay test completed!')
