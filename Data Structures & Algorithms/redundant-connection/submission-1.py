class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par = {}
        self.rank = {}
        for i in range(len(edges)):
            k = i+1
            self.par[k] = k
            self.rank[k]=0
        def find(x):
            if self.par[x]!=x:
                self.par[x] = find(self.par[x])
            return self.par[x]
        for edge in edges:
            x = edge[0]
            y = edge[1]
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return edge
            if self.rank[rootx]<self.rank[rooty]:
                self.par[rootx] = rooty
            elif self.rank[rootx]>self.rank[rooty]:
                self.par[rooty] = rootx
            else:
                self.par[rooty] = rootx
                self.rank[rootx]+=1
        return []

