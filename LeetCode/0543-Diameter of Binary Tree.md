---
title: 0543-Diameter of Binary Tree
updated: 2022-06-26 14:12:35Z
created: 2022-06-26 14:11:29Z
source: https://leetcode.com/problems/diameter-of-binary-tree/
tags:
  - binary tree
  - easy
  - python
  - recursion
---

543\. Diameter of Binary Tree

Easy

Given the `root` of a binary tree, return *the length of the **diameter** of the tree*.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](../_resources/diamtree_0957a2a2558e4d10a7a3148139ceb4bb.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

```

**Example 2:**

```
Input: root = [1,2]
Output: 1

```

**Constraints:**

- The number of nodes in the tree is in the range `[1, 10<sup>4</sup>]`.
- `-100 <= Node.val <= 100`

**Solution:**
```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, result = self.diameter(root)
        return result -1
    
    def diameter(self, root):
        if root is None:
            return 0, 0
        left = self.diameter(root.left)
        right = self.diameter(root.right)
        
        longestPathThisNode = left[0] + right[0] + 1
        longestPathThisSubtree = max(left[1], right[1])
        longestPathThisSubtree = max(longestPathThisSubtree, longestPathThisNode)
        height = 1 + max(left[0], right[0])
        return height, longestPathThisSubtree
```
Time Complexity:O(n), where n is the number of nodes
Space Complexity:O(height), used on the recursionstack