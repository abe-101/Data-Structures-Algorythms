---
title: 0207- Course Schedule
updated: 2022-07-05 17:39:42Z
created: 2022-07-05 17:39:08Z
source: https://leetcode.com/problems/course-schedule/
tags:
  - dfs
  - graph
  - medium
  - python
---

207\. Course Schedule

Medium

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that you **must** take course `b<sub>i</sub>` first if you want to take course `a<sub>i</sub>`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

```

**Example 2:**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses`
- All the pairs prerequisites\[i\] are **unique**.

**Solution:**
```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def cycle_detect(graph, node, visitng, visited):
            if node in visited:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)
            for neighbor in graph[node]:
                if cycle_detect(graph, neighbor, visiting, visited):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False
        
        def build_graph(numCourses, prerequisites):
            graph = {}
            for i in range(0, numCourses):
                graph[i] = []
            for prereq in prerequisites:
                a, b = prereq
                graph[a].append(b)
            return graph
        
        graph = build_graph(numCourses, prerequisites)
        visited = set()
        visiting = set()
        for node in graph:
            if cycle_detect(graph, node, visiting, visited):
                return False
        return True