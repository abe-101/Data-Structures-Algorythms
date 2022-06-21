#!/usr/bin/python3
"""
tree value count

Write a function, tree_value_count, that takes in the
root of a binary tree and a target value. The function
should return the number of times that the target
occurs in the tree.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# DFS Recursive
# def tree_value_count(root, target):
#     # Time: O(n)
#     # Space: O(n)
#     if root is None:
#         return 0
#     match = 1 if root.val == target else 0
# 
#     return match + tree_value_count(root.left, target) + tree_value_count(root.right, target)

# DFS Iterative
def tree_value_count(root, target):
    # Time: O(n)
    # Space: O(n)
    if root is None:
        return 0

    count = 0
    stack = [ root ] 
    while stack:
        current = stack.pop()
        if current.val == target:
            count += 1

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return count

# test_00:

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4   6     12

assert(tree_value_count(a,  6) == 3)

# test_01:

a = Node(12)
b = Node(6)
c = Node(6)
d = Node(4)
e = Node(6)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      12
#    /   \
#   6     6
#  / \     \
# 4  6     12

assert(tree_value_count(a,  12) == 2)

# test_02:

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

assert(tree_value_count(a, 1) == 4)

# test_03:

a = Node(7)
b = Node(5)
c = Node(1)
d = Node(1)
e = Node(8)
f = Node(7)
g = Node(1)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      7
#    /   \
#   5     1
#  / \     \
# 1   8     7
#    /       \
#   1         1

assert(tree_value_count(a, 9) == 0)

# test_04:

assert(tree_value_count(None, 42) == 0)
print('--Yay all tests passed!')
