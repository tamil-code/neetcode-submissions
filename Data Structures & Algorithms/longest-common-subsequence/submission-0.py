class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        t1 = "#" + text1
        t2 = '#' + text2
        row = len(t1)
        col = len(t2)
        dp = [[0]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if t1[i]=="#" or t2[j]=="#":
                    continue
                if t1[i]==t2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[row-1][col-1]