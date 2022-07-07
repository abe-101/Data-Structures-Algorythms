---
title: 0112-Path Sum
updated: 2022-06-23 13:29:20Z
created: 2022-06-23 13:27:16Z
source: https://leetcode.com/problems/path-sum/
tags:
  - binary tree
  - easy
  - iterative
  - python
  - recursion
---

112\. Path Sum

Easy

Given the `root` of a binary tree and an integer `targetSum`, return `true` if the tree has a **root-to-leaf** path such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

**Example 1:**

<img width="500" height="356" src="../_resources/pathsum1_94d5684d057e40dc811fefc5d818507e.jpg"/>

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

```

**Example 2:**

![](../_resources/pathsum2_caea8e19fd664da383af666bbe12f7a4.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

```

**Example 3:**

```
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

**Solution:**
Recursive:
```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if root.left is None and root.right is None and root.val - targetSum == 0:
                return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
```
Iterative:
```python
lass Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stack = [(root, root.val)]
        
        while stack:
            node, sumval = stack.pop()
            if sumval == targetSum and not node.left and not node.right:
                return True
            if node.right:
                stack.append((node.right, sumval + node.right.val))
            if node.left:
                stack.append((node.left, sumval + node.left.val))
        return False
```