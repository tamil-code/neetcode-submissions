from collections import deque,defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()
        count = 0 # how many node we're going to in bfs + indegree using toposort
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]]+=1
        for idx,i in enumerate(indegree):
            if i==0:
                queue.append(idx)
        while queue:
            node = queue.popleft()
            count+=1
            print("node",node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        print("count: ",count)
        print("adj",adj)
        return count==numCourses

