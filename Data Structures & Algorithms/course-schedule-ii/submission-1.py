class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses
        queue = deque()
        course_order = [] 
        count=0
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]]+=1
        for idx,i in enumerate(indegree):
            if i==0:
                queue.append(idx)
        while queue:
            node = queue.popleft()
            course_order.append(node)
            count+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
  
        return course_order if count==numCourses else []      