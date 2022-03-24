---
title: 2-Queue-Using-2-Stacks
updated: 2022-03-23 14:26:20Z
created: 2022-03-22 19:27:18Z
tags:
  - medium
  - stack
---

## **Queue Using 2 Stacks**

<ins>**Level**: Medium</ins>

Implement a Queue using 2 stacks.

Questions to Clarify:  
Q. Can we use extra memory?  
A. Use only constant memory - O(1)  

Q. What to return if the user tries to dequeue an empty queue?  
A. Throw an exception.  

## Solution

**Pseudocode**:

```
enqueue():
    if s2 is empty
        flush from s1 to s2
    if s2 is still empty
        queue is empty, return nothing
    
    return s2.pop()
```

<ins>Test Cases:</ins>
Edge Cases: Enqueue with empty, Dequeue with empty  
Base Cases: Enqueue with 1 element, dequeue with 1 element  
Regular Cases: Dequeue with stack 2 empty, Multiple dequeues/enqueues in a row  

Time Complexity:  

Enqueue: O(1)  
Dequeue: O(n) in the worst case, O(1) amortized

Space Complexity: O(1) extra space  

**code:**

```java
public class Queue [{<br>Stack](#) [s1;<br>Stack](#) [s2;](#)

public Queue() {
    s1 = new Stack<A>();
    s2 = new Stack<A>();
}

public void enqueue(A a) {
    s1.push(a);
}

public A dequeue() throws EmptyQueueException {
    if (s2.isEmpty()) {
        flushToS2();
    }
    if (s2.isEmpty()) {
        throw new EmptyQueueException();
    }

    return s2.pop();
}

private void flushToS2() {
    while (!s1.isEmpty()) {
        s2.push(s1.pop());
    }
} 


}

public class EmptyQueueException extends Exception {
    public EmptyQueueException() {
    }
}
```