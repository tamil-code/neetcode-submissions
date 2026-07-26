from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
        visited = set()
        def isCycle(node,parent):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if isCycle(nei,node):
                        return True
                elif nei!=parent:
                    return True
            return False

        return not isCycle(0,-1) and len(visited)==n
            