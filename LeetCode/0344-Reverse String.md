---
title: 0344-Reverse String
updated: 2022-06-13 18:03:09Z
created: 2022-06-13 18:02:19Z
source: https://leetcode.com/problems/reverse-string/
tags:
  - easy
  - python
  - two pointers
---

344\. Reverse String

Easy

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

**Example 1:**

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

```

**Example 2:**

```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

```

**Constraints:**

- `1 <= s.length <= 10<sup>5</sup>`
- `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).

**Solution:**
```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s) - 1
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
```

Time Complexity: O(n)
Space Complexity: O(1)