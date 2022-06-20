#!/usr/bin/python3
"""
zipper lists

Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def zipper_lists(head_1, head_2):
    # Time: O(min(n, m))
    # Space: O(1)
    origin = head_1
    target = head_2
    while target is not None:
      tmp = origin.next
      origin.next = target
      origin = target
      target = tmp
    return head_1

# test_00:
a = Node("a")
b = Node("b")
c = Node("c")
a.next = b
b.next = c
# a -> b -> c
x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z
assert(zipper_lists(a, x) == a)
# a -> x -> b -> y -> c -> z
# test_01:
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
# a -> b -> c -> d -> e -> f
x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z
assert(zipper_lists(a, x) == a)
# a -> x -> b -> y -> c -> z -> d -> e -> f
# test_02:
s = Node("s")
t = Node("t")
s.next = t
# s -> t
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
one.next = two
two.next = three
three.next = four
# 1 -> 2 -> 3 -> 4
assert(zipper_lists(s, one) == s)
# s -> 1 -> t -> 2 -> 3 -> 4
# test_03:
w = Node("w")
# w
one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 
assert(zipper_lists(w, one) == w)
# w -> 1 -> 2 -> 3
# test_04:
one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three
# 1 -> 2 -> 3 
w = Node("w")
# w
assert(zipper_lists(one, w) == one)
# 1 -> w -> 2 -> 3

print('-- Yay test completed!')
