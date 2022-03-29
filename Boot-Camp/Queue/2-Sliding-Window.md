---
title: 2-Sliding-Window
updated: 2022-03-28 15:06:11Z
created: 2022-03-28 14:48:28Z
tags:
  - easy
  - queue
---

## **Sliding Window**

<ins>**Level**: Easy</ins>
Given an array of integers A, find the sum of each sliding window of size K.
Variation:​ Instead of an array, what if you were presented with a ​stream​ of numbers. A new number
can be added anytime. You want to find the sum of the last K elements.

Questions to Clarify:
Q. Is K provided as input?
A. Yes.

Q. How do you want the output?
A. Print the sum of each sliding window.

## Solution

Whenever you see a sliding window problem, you should think of using a queue.
We keep adding elements to the queue until it is of size K. To add another element, we remove the element from the back and add the new element to the front, maintaining the size K of the queue.
Every time we add an element, we add its value to the sum. When we remove an element, we subtract its value from the sum. That way, the sum always contains the sum of the sliding window of size K.

**Pseudocode**:

```
init Queue
init sum = 0
loop i through A:
    if (Queue size is K)
        remove element E from front
        sum = sum - E
    add A[i] to Queue
    sum = sum + A[i]
    if (Queue size is K)
        print sum to output
```

<ins>Test Cases:</ins>
Edge Cases: array empty, K is 0, K is 1
Base Cases: K is 2, array size is 1
Regular Cases: K is 3 or more, K is less than array size

Time Complexity: O(n)
Space Complexity: O(K), because we store at most K nodes in the queue

**code:**

```java
public static void slidingWindowSum(int[] a, int k) {
	if (a == null || k == 0 || a.length == 0)
		return;
	
	// LinkedList implements Queue interface in Java
	Queue<Integer> q = new LinkedList<>();
	int sum = 0;
	for (int i = 0; i <a.length; i++) {
		if (q.size() == k) {
			int last = q.remove();
			sum -= last;
		}
		q.add(a[i]);
		sum += a[i];
		if (q.size() == k) {
			System.out.print(sum);
		}
	}
}
```