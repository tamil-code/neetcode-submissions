class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "#"+word1
        word2 = "#"+word2
        row = len(word1)
        col = len(word2)
        min_dist = [[0]*col for _ in range(row)]
        for i in range(row):
            min_dist[i][0] = i
        for j in range(col):
            min_dist[0][j] = j
        for i in range(row):
            for j in range(col):
                if word1[i]=="#" or word2[j]=="#":
                    continue
                if word1[i]==word2[j]:
                    min_dist[i][j] = min_dist[i-1][j-1]
                else:
                    res = min(min_dist[i-1][j-1],min_dist[i-1][j])
                    min_dist[i][j] = 1 + min(res,min_dist[i][j-1])
        return min_dist[row-1][col-1]