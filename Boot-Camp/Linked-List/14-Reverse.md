---
title: 14-Reverse
updated: 2022-03-22 16:01:09Z
created: 2022-03-22 14:58:29Z
tags:
  - easy
  - linked list
---

## **Reverse**

<ins>**Level**:Easy</ins>
Reverse a linked list. You should use O(1) space.

Questions to Clarify:
Q. Is is a singly linked list?
A. Yes

Q. How do you want the output?
A. Return the new head of the linked list.

## Solution

We simply rearrange the next pointers to do the reversal.

**Pseudocode**:

```
prev = null
curr = head
while curr != null
    Node next = curr.next
    curr.next = prev
    prev = curr
    curr = next
```

<ins>Test Cases:</ins>
Edge Cases: Empty list
Base Cases: Single node, 2 nodes
Regular Cases: > 2 nodes

Time Complexity: O(n)
Space Complexity: O(1)

**code:**

```
public static Node reverse(Node head) {
    Node prev = null, cur = head;
    While (curr != null) {
        Node next = curr.getNext();
        curr.setNext(prev);
        prev = curr;
        curr = next;
    }
    return prev;
}
```