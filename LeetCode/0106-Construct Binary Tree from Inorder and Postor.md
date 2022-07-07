---
title: 0106-Construct Binary Tree from Inorder and Postorder Traversal
updated: 2022-06-23 14:57:45Z
created: 2022-06-23 14:45:28Z
source: >-
  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
tags:
  - binary tree
  - medium
  - python
  - recursion
---

106\. Construct Binary Tree from Inorder and Postorder Traversal

Medium

Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and `postorder` is the postorder traversal of the same tree, construct and return *the binary tree*.

**Example 1:**

![](../_resources/tree_774f34865d7b4c7796283bd27fcbd3a5.jpg)

```
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

```

**Example 2:**

```
Input: inorder = [-1], postorder = [-1]
Output: [-1]

```

**Constraints:**

- `1 <= inorder.length <= 3000`
- `postorder.length == inorder.length`
- `-3000 <= inorder[i], postorder[i] <= 3000`
- `inorder` and `postorder` consist of **unique** values.
- Each value of `postorder` also appears in `inorder`.
- `inorder` is **guaranteed** to be the inorder traversal of the tree.
- `postorder` is **guaranteed** to be the postorder traversal of the tree.

**Solution:**
```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return
        
        root = TreeNode(postorder.pop())
        mid = inorder.index(root.val)
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        return root
```

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i
            
        def _buildTree(low, high):
            if low > high:
                return
        
            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = _buildTree(mid+1, high)
            root.left = _buildTree(low, mid-1)
            return root
        return _buildTree(0, len(inorder)-1)
```