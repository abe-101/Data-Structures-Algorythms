---
title: 10-Find-Median
updated: 2022-03-15 15:05:57Z
created: 2022-03-15 14:56:56Z
---

## **Find Median**

<ins>**Level**: Medium</ins>
Find the median node of a linked list. For example:
1 -> 2 -> 3 -> 4 -> 5  Median node is 3.

Questions to Clarify:
Q. If there are even number of nodes, which node to return?
A. Return either one of the 2 middle nodes.

## Solution
We use a slow pointer and a fast pointer until the fast pointer reaches the end
of the list. If the slow pointer is moving at half the pace of the fast pointer,
it will be pointing to the median.

**Pseudocode**:
```
median(head, tail)
    fast = head, slow = head
    while (fast.next != null)
        fast = fast.next
        if (fast.next != null)
            fast = fast.next
            slow = slow.next
    return slow
```
<ins>Test Cases:</ins>
Edge Cases: empty list  
Base Cases: single node list  
Regular Cases: 2 nodes, 3 nodes, odd, even  

Time Complexity: O(n)  
Space Complexity: O(1)  

**code:**
```
public static Node findMedian(Node head, Node tail) {
    if (head == null || tail == null)
        return null;
    Node fast = head, slow = head;
    While(fast.getNext() != null) {
        fast = fast.getNext();
        if (fast.getNext() != null) {
            fast = fast.getNext();
            slow = slow.getNext();
        }
    }
    return slow;
}
``` 
