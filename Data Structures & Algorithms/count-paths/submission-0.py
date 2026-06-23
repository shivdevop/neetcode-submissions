class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #we can create a grid resembling the maze but it will be a dp matrix, each cell storing number of ways we can reach that cell 
        dp=[[0 for _ in range(n)]for _ in range(m)]

        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                up=0
                left=0
                if 0<=i-1:
                    up=dp[i-1][j]
                if j-1>=0:
                    left=dp[i][j-1]

                dp[i][j]=up+left

        return dp[m-1][n-1]                    
        