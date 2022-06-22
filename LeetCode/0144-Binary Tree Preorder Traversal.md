---
title: 0144-Binary Tree Preorder Traversal
updated: 2022-06-22 18:16:59Z
created: 2022-06-22 17:23:27Z
source: https://leetcode.com/problems/binary-tree-preorder-traversal/
tags:
  - binary tree
  - iterative
  - python
  - recursion
---

144\. Binary Tree Preorder Traversal

Easy

Given the `root` of a binary tree, return *the preorder traversal of its nodes' values*.

**Example 1:**

<img width="125" height="201" src="../_resources/inorder_1_f116ccd9677b40348c9d6dd5847af152.jpg" class="jop-noMdConv">

```
Input: root = [1,null,2,3]
Output: [1,2,3]

```

**Example 2:**

```
Input: root = []
Output: []

```

**Example 3:**

```
Input: root = [1]
Output: [1]

```

**Constraints:**

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

**Solution:**
Recursion:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self._preorderTraversal(root, result)
        return result

        
    def _preorderTraversal(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        result.append(root.val)
        self._preorderTraversal(root.left, result)
        self._preorderTraversal(root.right, result)
```

Iterative:

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [ root ]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
```