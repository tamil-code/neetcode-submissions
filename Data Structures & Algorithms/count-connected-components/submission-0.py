from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        visited = set()
        component = 0
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                component+=1
                dfs(node)
        return component
