# problem: https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
"""
Algo:
Topological sort + merge ancestors 
toplogocal sort takes O(n), merge worst case takes O(n)
Overall: O(n^2) algo
"""
from collections import defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = dict()
        count = dict()
        for i in range(n):
            indegree[i] = 0
            count[i] = set()
        for e in edges:
            indegree[e[1]] += 1
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
        src = []
        for x in indegree:
            if indegree[x] == 0:
                src.append(x)
        while src:
            node = src.pop(0)
            for nei in graph[node]:
                indegree[nei] -= 1
                count[nei] = count[nei].union(count[node])
                count[nei].add(node)
                if indegree[nei] == 0:
                    src.append(nei)
        result = []
        for i in range(n):
            if len(count[i]) == 0:
                result.append([])
                continue
            result.append(sorted(count[i]))
        return result