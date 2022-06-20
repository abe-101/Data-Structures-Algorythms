#!/usr/bin/python3
"""
tree sum

Write a function, tree_sum, that takes in the root of a binary tree that
contains number values. The function should return the total sum of all values
in the tree.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# def tree_sum(root):
#     if root is None:
#         return 0
#     return root.val + tree_sum(root.left) + tree_sum(root.right)

from collections import deque

def tree_sum(root):
    if not root:
        return 0

    queue = deque([ root ])
    total_sum = 0

    while queue:
        node = queue.popleft()

        total_sum += node.val

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return total_sum


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

assert(tree_sum(a) == 21)


# test_01:

a = Node(1)
b = Node(6)
c = Node(0)
d = Node(3)
e = Node(-6)
f = Node(2)
g = Node(2)
h = Node(2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

assert(tree_sum(a) == 10)


# test_02:

tree_sum(None) # -> 0
print('--Yay all tests passed!')
