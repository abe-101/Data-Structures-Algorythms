---
title: 0110-Balanced Binary Tree
updated: 2022-06-24 14:50:22Z
created: 2022-06-24 14:48:42Z
source: https://leetcode.com/problems/balanced-binary-tree/
tags:
  - binary tree
  - easy
  - python
  - recursion
---

110\. Balanced Binary Tree

Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.

**Example 1:**

![](../_resources/balance_1_1ddefcf061a24d3a8ae344e7d6785542.jpg)

```
Input: root = [3,9,20,null,null,15,7]
Output: true

```

**Example 2:**

![](../_resources/balance_2_91550d9242ce4b9cbceb6f9e6dcd5a02.jpg)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

```

**Example 3:**

```
Input: root = []
Output: true

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10<sup>4</sup> <= Node.val <= 10<sup>4</sup>`

**Solution:**
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._isBalanced(root) != -1 
    
    def _isBalanced(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self._isBalanced(root.left)
        right = self._isBalanced(root.right)
        
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(self._isBalanced(root.left), self._isBalanced(root.right))
```