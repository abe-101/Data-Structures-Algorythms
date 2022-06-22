---
title: 0094-Binary Tree Inorder Traversal
updated: 2022-06-22 16:45:54Z
created: 2022-06-22 16:44:00Z
source: https://leetcode.com/problems/binary-tree-inorder-traversal/
tags:
  - binary tree
  - dfs
  - iterative
  - python
  - recursion
---

94\. Binary Tree Inorder Traversal

Easy

Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

**Example 1:**

<img width="125" height="201" src="../_resources/inorder_1_ab84ed64ef2d4fa69098db71d124430d.jpg"/>

```
Input: root = [1,null,2,3]
Output: [1,3,2]

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        self._inorderTraversal(root, result)
        return result

        
    def _inorderTraversal(self, root: Optional[TreeNode], result: List[int]):
        if root is None:
            return
        self._inorderTraversal(root.left, result)
        result.append(root.val)
        self._inorderTraversal(root.right, result)
```

iterative:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
```