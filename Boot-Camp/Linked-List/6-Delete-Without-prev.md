---
title: 6-Delete-Without-prev
updated: 2022-03-14 19:24:53Z
created: 2022-03-14 19:05:22Z
tags:
  - easy
  - linked list
---

## Delete Without Prev

<ins>**Level**: Easy</ins>

Follow Up: Given a node N in a Linked List, can you delete it without the
previous node in O(1) time?

Questions to Clarify:
Q. Is okay to just remove the val but not delete the node?
A. Yes.

## Solution

We can copy over the next node's value int N, and then delete the next node.

**Pseudocode**:

```
delete(head, tail, N)
    if n is tail, return
    copy value from N.next
    delete N.next
```

<ins>Test Cases:</ins>
Edge Cases: List Empty, N is tail, N is head
Base Cases: Single Item List
Regular Cases: N is in middle
Time Complexity: O(1)
Space Complexity: O(1)

**code:**

```java
public void deleteWithoutPrev(Node n) {
    Node next = n.getNext();
    if (next == null)
        return // cannot delete

    n.setData(next.getData());
    delete(next, n);
}

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