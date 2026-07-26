from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,dst,time in times:
            adj[src].append((dst,time))
        shortest_path_cost = {} # it holds cost to reach each node from source
        min_heap = [(0,k)]
        while min_heap:
            time,node = heappop(min_heap)
            if node in shortest_path_cost:
                continue
            shortest_path_cost[node] = time
            for neighbour,n_time in adj[node]:
                if neighbour not in shortest_path_cost:
                    heappush(min_heap,(time+n_time,neighbour))
        if len(shortest_path_cost)!=n:
            return -1
        print(shortest_path_cost)
        return max(shortest_path_cost.values())
        
        