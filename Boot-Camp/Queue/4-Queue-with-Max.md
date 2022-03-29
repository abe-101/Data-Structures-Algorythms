---
title: 4-Queue-with-Max
updated: 2022-03-29 14:56:38Z
created: 2022-03-29 14:15:59Z
tags:
  - hard
  - queue
---

## **Queue With Max**

<ins>**Level**: Hard</ins>

Implement a Queue with O(1) lookup of the Maximum element.

Questions to Clarify:
Q. Can we assume that it will have integers?
A. Yes

## Solution

We use a similar approach as stacks - keep two queues - a main queue and a max queue.
The main queue contains the elements. The max queue contains the max elements. The max queue is a double ended queue (deque) because we want to be able to remove elements from both ends.

**Pseudocode**:

```
init main queue and max queue

enqueue(n)
    main.enqueue(n)
    while (max.back < n)
        max.remove_back()
    max.enqueue(n)

dequeue()
    value = main.deque()
    if (max.front() == value)
        max.dequeue()

findMax()
    return max.front()
```

<ins>Test Cases:</ins>
Edge Cases: empty queue
Base Cases: single element in queue
Regular Cases: insert equal element as back, remove equal element,
elements in decreasing/increasing order

Insertion: O(n) worse case, O(1) amortized because we remove at most N elements for N insertions.
Deletion and Max lookup: O(1)

**code:**

```java
public class QueueWithMax {
    Queue<Integer> main;
    Deque<Integer> max;
    
    public QueueWithMax() {
        main = new LinkedList<>();
        max = new LinkedList<>();
    }
    
    public void enqueue(int item) {
        main.add(item);
        while (!max.isEmpty() && max.getLast() < item)
            max.removeLast();
        max.add(item);
    }
    
    public void dequeue() throws QueueEmptyException {
        if (main.isEmpty())
            throw new QueueEmptyException();
        int item = main.remove();
        if (max.getFirst() == item)
            max.remove();
    }
    
    public int findMax() throws QueueEmptyException {
        if (max.isEmpty())
            throw new QueueEmptyException();
        return max.getFirst();
    }
}
```