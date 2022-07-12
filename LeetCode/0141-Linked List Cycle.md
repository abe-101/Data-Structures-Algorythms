---
title: 0141-Linked List Cycle
updated: 2022-07-11 12:12:51Z
created: 2022-07-11 12:12:05Z
source: https://leetcode.com/problems/linked-list-cycle/
---

141\. Linked List Cycle

Easy

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**

<img width="300" height="97" src="../_resources/circularlinkedlist_4fb26d64b4474553ae0951a50fcdc27.png"/>

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

**Example 2:**

<img width="141" height="74" src="../_resources/circularlinkedlist_test2_de6983c1fe144527af08378f1.png"/>

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

```

**Example 3:**

<img width="45" height="45" src="../_resources/circularlinkedlist_test3_12b405bc183a434788e77a049.png"/>

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

```

**Constraints:**

- The number of the nodes in the list is in the range `[0, 10<sup>4</sup>]`.
- `-10<sup>5</sup> <= Node.val <= 10<sup>5</sup>`
- `pos` is `-1` or a **valid index** in the linked-list.

**Follow up:** Can you solve it using `O(1)` (i.e. constant) memory?

**Solution:**
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        first_iteration = True
        while fast and fast.next:
            if slow is fast and not first_iteration:
                return True
            slow = slow.next
            fast = fast.next.next
            first_iteration = False
        return False
```
Time Complexity: O(n)
Space Complexity: O(1)