---
title: 5-Sliding-Window-Max
updated: 2022-03-29 14:57:37Z
created: 2022-03-29 14:34:48Z
tags:
  - hard
  - queue
  - sliding window
---

## **Sliding Window Max**

<ins>**Level**: Hard</ins>
Maximum of Sliding Window​: Given an array A and an integer K, find the maximum element in each sliding window of size K.  
For example,  
if A = \[4,6,5,2,4,7\] and K = 3, windows are as follows:  

\[​4,6,5​,2,4,7\] : Max = 6  
\[4,​6,5,2​,4,7\] : Max = 6  
\[4,6,​5,2,4​,7\] : Max = 5  
\[4,6,5,​2,4,7​\] : Max = 7  

Output: 6,6,5,7  

Hint​: You can do this in O(n) time, by using the ​Queue with Max​ technique.  

Questions to Clarify:
Q. How should we output the result?  
A. Print the max of each sliding window.  

Q. What if A is empty or null?  
A. Print nothing.  

Q. What if K is 0?  
A. Print nothing.  

## Solution

This is a straightforward application of a Queue with Max. Maintain a Queue with Max and simply output the max after processing each element.

**Pseudocode**:

```
SlidingWindowMax(int[] a, int k)
    q = new queueWithMax

    add forst k elements to the queue
    print out first window max

    for: i = k to a.length - 1:
        add a[i]
        deque q
        print out max element
```

<ins>Test Cases:</ins>
Edge Cases: empty array, null array, k=0  
Base Cases: single element array, k=1  
Regular Cases: multiple elements (k=2, k=3)  

Time Complexity:​ O(n)  
Space Complexity:​ O(k) - the queue with max will store up to K elements  
**code:**

```java
public static void slidingWindowMax(int[] a, int windowSize) {
    if (a == null || a.length == 0 || windowSize <= 0)
        return;
    
    QueueWithMax q = new QueueWithMax();
    
    try {
        // add first k elements
        for (int i = 0; i < windowssize; i++) {
            q.enqueue(a[i]);
        }
        system.out.println(q.findMax());
        
        // add the rest one by one
        for (int i = windowSize; i < a.length; i++) {
            q.dequeue();
            q.enqueue(a[i]);
            system.out.println(q.findMax());
        }
    } catch (QueueEmptyException e) {
        // should not happen
        e.printStackTrace();
    }
}

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