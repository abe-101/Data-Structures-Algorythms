#!/usr/bin/python3
"""
Write a function, create_linked_list, that takes in a list of values as an
argument. The function should create a linked list containing each item of the
list as the values of the nodes. The function should return the head of the
linked list.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def create_linked_list(values):
    # Time: O(n)
    # Space: O(n)
    dummy_head = Node(None)
    tail = dummy_head
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy_head.next

# Recursive
def create_linked_list(values, i = 0):
    # Time: O(n)
    # Space: O(n)
    if i == len(values):
        return None
    head = Node(values[i])
    head.next = create_linked_list(values, i + 1)
    return head



# TESTS
# return linked list as a list
def linked_list(head):
    if head is None:
        return None
    current = head
    result = []
    while current is not None:
        result.append(str(current.val))
        current = current.next
    return result

# test_00:

assert(linked_list(create_linked_list(["h", "e", "y"])) == list('hey'))
# h -> e -> y

# test_01:

assert(linked_list(create_linked_list([1, 7, 1, 8])) == list('1718'))
# 1 -> 7 -> 1 -> 8

# test_02:

assert(linked_list(create_linked_list(["a"])) == list('a'))
# a

# test_03:

assert(linked_list(create_linked_list([])) == None)
# null

print('-- Yay test completed!')
