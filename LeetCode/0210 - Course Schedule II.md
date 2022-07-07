---
title: 0210 - Course Schedule II
updated: 2022-07-05 18:38:34Z
created: 2022-07-05 18:37:52Z
source: https://leetcode.com/problems/course-schedule-ii/
tags:
  - dfs
  - graph
  - medium
  - python
---

210\. Course Schedule II

Medium

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` indicates that you **must** take course `b<sub>i</sub>` first if you want to take course `a<sub>i</sub>`.

- For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return *the ordering of courses you should take to finish all courses*. If there are many valid answers, return **any** of them. If it is impossible to finish all courses, return **an empty array**.

**Example 1:**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

```

**Example 2:**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

```

**Example 3:**

```
Input: numCourses = 1, prerequisites = []
Output: [0]

```

**Constraints:**

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses`
- `a<sub>i</sub> != b<sub>i</sub>`
- All the pairs `[a<sub>i</sub>, b<sub>i</sub>]` are **distinct**.

**Solution:**

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:       
        def dfsVisit(graph, node, visiting, visited, result):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for neighbor in graph[node]:
                if dfsVisit(graph, neighbor, visiting, visited, result) == False:
                    return False
                
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
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
        result = []
        for node in graph:
            if dfsVisit(graph, node, visiting, visited, result) == False:
                return []
        return result
```