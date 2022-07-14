---
title: 0003-Longest Substring Without Repeating Characters
updated: 2022-07-13 15:16:21Z
created: 2022-07-13 15:15:42Z
source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
tags:
  - blind 75
  - medium
  - python
  - sliding window
---

3\. Longest Substring Without Repeating Characters

Medium

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**

```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

```

**Example 2:**

```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

**Example 3:**

```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

**Constraints:**

- `0 <= s.length <= 5 * 10<sup>4</sup>`
- `s` consists of English letters, digits, symbols and spaces.

**Solution:**
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)
            
        return result
```
Time Complexity: O(n)
Space Complexity: O(n)