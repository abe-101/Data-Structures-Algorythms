#!/usr/bin/python3

"""
Write a function, breadth_first_values, that takes in the root of a binary
tree. The function should return a list containing all values of the tree in
breadth-first order.
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root):
    if not root:
        return []

    queue = deque([ root ])
    values = []

    while queue:
        node = queue.popleft()

        values.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return values

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

assert(breadth_first_values(a) == ['a', 'b', 'c', 'd', 'e', 'f'])

# test_01:

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

breadth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# test_02:

a = Node('a')

#      a

assert(breadth_first_values(a) == ['a'])

# test_03:

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

assert(breadth_first_values(a) == ['a', 'b', 'c', 'x', 'd', 'e'])

# test_04:

breadth_first_values(None) 
#    -> []
print('--Yay all tests passed!')
