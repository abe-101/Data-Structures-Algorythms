#!/usr/bin/python3
"""
Write a function, remove_node, that takes in the head of a linked list and a
target value as arguments. The function should delete the node containing the
target value from the linked list and return the head of the resulting linked
list. If the target appears multiple times in the linked list, only remove the
first instance of the target in the list.

Do this in-place.

You may assume that the input list is non-empty.

You may assume that the input list contains the target.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Iterative
def remove_node(head, target_val):
    # Time: O(n)
    # Space: O(1)
    if head.val == target_val:
        return head.next
    current = head
    prev = None
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head
    
# Recursive
def remove_node(head, target_val):
    # Time: O(n)
    # Space: O(n)
    if head is None:
        return None
    if head.val == target_val:
        return head.next
    head.next = remove_node(head.next, target_val)
    return head



# test_00:
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
assert(remove_node(a, "c") == a)
# a -> b -> d -> e -> f
# test_01:
x = Node("x")
y = Node("y")
z = Node("z")
x.next = y
y.next = z
# x -> y -> z
assert(remove_node(x, "z") == x)
# x -> y
# test_02:
q = Node("q")
r = Node("r")
s = Node("s")
q.next = r
r.next = s
# q -> r -> s
assert(remove_node(q, "q") == r)
# r -> s
# test_03:
node1 = Node("h")
node2 = Node("i")
node3 = Node("j")
node4 = Node("i")
node1.next = node2
node2.next = node3
node3.next = node4
# h -> i -> j -> i
assert(remove_node(node1, "i") == node1)
# h -> j -> i
# test_04:
t = Node("t")
# t
assert(remove_node(t, "t") ==  None)
print('-- Yay test completed!')
