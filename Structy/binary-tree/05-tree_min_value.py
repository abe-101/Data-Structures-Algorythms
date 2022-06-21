#!/usr/bin/python3
"""
tree min value

Write a function, tree_min_value, that takes in the root of a binary tree that
contains number values. The function should return the minimum value within the
tree.

You may assume that the input tree is non-empty.

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_min_value(root):
    if root is None:
        return float("inf")
    smallest_left_value = tree_min_value(root.left)
    smallest_right_value = tree_min_value(root.right)
    return min(root.val, smallest_left_value, smallest_right_value)

# test_00:

a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
assert(tree_min_value(a) == -2)

# test_01:

a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

assert(tree_min_value(a) == 3)

# test_02:

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2

assert(tree_min_value(a) == -13)

# test_03:

a = Node(42)

#        42

assert(tree_min_value(a) == 42)

print('--Yay all tests passed!')
