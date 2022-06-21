#!/usr/bin/python3
"""
bottom right value

Write a function, bottom_right_value, that takes in the root of a binary tree.
The function should return the right-most value in the bottom-most level of the
tree.

You may assume that the input tree is non-empty.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque

# Iterative
def bottom_right_value(root):
    # Time:
    # Space:
    queue = deque([ root ])
    current = None

    while queue:
        current = queue.popleft()

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return current.val

# test_00:

a = Node(3)
b = Node(11)
c = Node(10)
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
#   11     10
#  / \      \
# 4   -2     1

assert(bottom_right_value(a) == 1)

# test_01:

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \       
#    -2  6

assert(bottom_right_value(a) == 6)

# test_02:

a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)
i = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 

assert(bottom_right_value(a) == 7)

# test_03

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.right = d
d.left = e
e.right = f

#      a
#    /   \ 
#   b     c
#    \
#     d
#    /
#   e
#  /
# f
          
assert(bottom_right_value(a) == 'f')

# test_04

a = Node(42)

#      42

assert(bottom_right_value(a) == 42)
print('--Yay all tests passed!')
