---
title: 5-Delete-Node
updated: 2022-03-14 19:21:10Z
created: 2022-03-14 17:37:04Z
---

## Delete Node

<ins>**Level**: Medium</ins>
Given a linked list and pointers to a node N and its previous node Prev, delete N from the linked list.

Questions to Clarify:
Q. Is N guaranteed to be in the list?
A. Yes

Q. What is Prev if N is the head?
A. Prev will be null

## Solution

If the node is head, we assign a new head. If it is tail, we assign the Previous node as the tail. Then, we assign Prev's next to N's next.

Note​: If Prev was not given, we would need to iterate through the linked list to find N's
previous node. That would take O(n) time.

**Pseudocode**:

```
delete (head, tail, N, prev)
    if N is head, head = N,next
    if N is tail, tail = prev
    prev.next = N.next
```

<ins>Test Cases:</ins>
Edge Cases: List empty, null values
Base Cases: Single element list, 2 element list
Regular Cases: N is head, tail, middle

Time Complexity: O(1)
Space Complexity: O(1)

**code:**

```
public void delete(Node n, Node prev) {
    if (n == null)
        return;

    if (n == head)
        head = n.getNext();
    else if (n == tail)
        tail = prev;

    if (prev != null)
        prev.setNext(n.getNext());
}
```