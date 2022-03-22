---
title: 8-Has-Cycle
updated: 2022-03-15 03:59:49Z
created: 2022-03-15 03:44:30Z
---

## **Has Cycle**

<ins>**Level**: Easy</ins>

Find if a given Linked List has a cycle.


Questions to Clarify:
Q. How do you want the output?
A. Return a boolean.

## Solution
One thing to note, if the list has a cycle, there will be no tail node.
We use a fast pointer and a slow pointer. If the two pointers meet, the list has a cycle..
If the fast pointer reaches the end of the list, there is no cycle.

**Pseudocode**:
```
init 2 pointers - fast and slow
while (end of list is not reached)
    advnace fast by 1 node
    return true if fast = slow
    advnace fast by 1 node
    return true if fast = slow
    advance slow by one node
end of list reached, return false
```
    
    
<ins>Test Cases:</ins>
Edge Cases: Empty list, one node list  
Base Cases: cycle of size 1, 2  
Regular Cases: no cycle, whole list is cycle/circular, part of list is cycle  

Time Complexity: O(n)  
Space Complexity: O(1)  

**code:**
```
public static boolean hasCycle(Node head) {
    Node fast = head, slow = head;
    while (fast != null) {
        fast = fast.getNext();
        if (fast == slow)
            return true;
        if (fast != null) {
            fast = fast.getNext();
            if (fast == slow)                
                return true;
        }
        slow = slow.getNext();
    }
    return false;
}
```
