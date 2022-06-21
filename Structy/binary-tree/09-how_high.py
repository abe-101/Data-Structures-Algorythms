#!/usr/bin/python3
"""
how high

Write a function, how_high, that takes in the root of
a binary tree. The function should return a number
representing the height of the tree.

The height of a binary tree is defined as the maximal
number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursive
def how_high(node):
    # Time: O(n)
    # Space: O(n)
    if not node:
        return -1
    return 1 + max(how_high(node.left), how_high(node.right))

# test_00:

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

assert(how_high(a) == 2)

# test_01:

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

assert(how_high(a) == 3)

# test_02:

a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

assert(how_high(a) == 1)

# test_03:

a = Node('a')

#      a

assert(how_high(a) == 0)

# test_04:

assert(how_high(None) == -1)
print('--Yay all tests passed!')
