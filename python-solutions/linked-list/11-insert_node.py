#!/usr/bin/python3
"""
Write a function, insert_node, that takes in the head of a linked list, a
value, and an index. The function should insert a new node with the value into
the list at the specified index. Consider the head of the linked list as index
0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater
than the length of the input list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def insert_node(head, value, index):
    # Time: O(n)
    # Space: O(1)
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head
    current = head
    count = 0
    while current is not None:
        if count == index -1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp
        count += 1
        current = current.next
    return head

# Recursive
#def
    # Time:
    # Space:


# TESTS
# return linked list as a list
def linked_list(head):
    current = head
    result = []
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d
assert(linked_list(insert_node(a, 'x', 2)) == list('abxcd'))
# a -> b -> x -> c -> d
# test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d
assert(linked_list(insert_node(a, 'v', 3)) == list('abcvd'))
# a -> b -> c -> v -> d
# test_02:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
a.next = b
b.next = c
c.next = d
# a -> b -> c -> d
assert(linked_list(insert_node(a, 'm', 4)) == list('abcdm'))
# a -> b -> c -> d -> m
# test_03:
a = Node("a")
b = Node("b")
a.next = b
# a -> b
assert(linked_list(insert_node(a, 'z', 0)) == list('zab'))
# z -> a -> b
print('-- Yay test completed!')
