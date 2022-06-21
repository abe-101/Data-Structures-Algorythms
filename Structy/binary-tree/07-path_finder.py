#!/usr/bin/python3
"""
tree path finder

Write a function, path_finder, that takes in the root of a binary tree and a
target value. The function should return an array representing a path to the
target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_finder(root, target):
    if root is None:
        return None

    if root.val == target:
        return [ root.val ]

    left_path = path_finder(root.left, target)
    if left_path:
        return [ root.val, * left_path ]

    right_path = path_finder(root.right, target)
    if right_path:
        return [ root.val, * right_path ]

    return None

# test_00:

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

assert(path_finder(a, 'e') == [ 'a', 'b', 'e' ])


# test_01:

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

assert(path_finder(a, 'p') == None)


# test_02:

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

assert(path_finder(a, "c") == ['a', 'c'])


# test_03:

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

assert(path_finder(a, "h") == ['a', 'c', 'f', 'h'])


# test_04:

x = Node("x")

#      x

assert(path_finder(x, "x") == ['x'])


# test_05:

assert(path_finder(None, "x") == None)

print('--Yay all tests passed!')
