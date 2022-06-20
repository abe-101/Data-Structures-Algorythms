#!/usr/bin/python3
"""
Write a function, tree_includes, that takes in the root of a binary tree and a
target value. The function should return a boolean indicating whether or not
the value is contained in the tree.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_includes(root, target):
    if not root:
        return False
    if root.val == target:
        return True

    return tree_includes(root.left, target) or tree_includes(root.right, target)


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

assert(tree_includes(a, "e") == True)

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
assert(tree_includes(a, "a") == True)

# test_02:

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

assert(tree_includes(a, "n") == False)

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

assert(tree_includes(a, "f") == True)

# test_04:

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

assert(tree_includes(a, "p") == False)

# test_05:

tree_includes(None, "b") == False
print('--Yay all tests passed!')
