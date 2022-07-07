---
title: '0101- Symmetric Tree '
updated: 2022-06-23 04:41:12Z
created: 2022-06-23 04:30:51Z
source: https://leetcode.com/problems/symmetric-tree/
tags:
  - binary tree
  - easy
  - python
  - recursion
---

101\. Symmetric Tree

Easy

Given the `root` of a binary tree, *check whether it is a mirror of itself* (i.e., symmetric around its center).

**Example 1:**

![](../_resources/symtree1_32a58b99b513458ca33c42e327b53e11.jpg)

```
Input: root = [1,2,2,3,4,4,3]
Output: true

```

**Example 2:**

![](../_resources/symtree2_581f9a723aaa4f3f881d0f48a93b8344.jpg)

```
Input: root = [1,2,2,null,3,null,3]
Output: false

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 1000]`.
- `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

**Solution:**
Rcursion:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root, root)
    
    def mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return(t1.val == t2.val) and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)
```

Iterative:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        
        q.append(root)
        q.append(root)
        
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            
            if node1 and not node2:
                return False
            if node2 and not node1:
                return False
            
            if not node2 and not node1:
                continue
                
            if node1.val != node2.val:
                return False
            
            q.append(node1.right)
            q.append(node2.left)
            q.append(node1.left)
            q.append(node2.right)
        return True
```