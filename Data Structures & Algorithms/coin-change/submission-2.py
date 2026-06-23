class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]

        #base cases 
        for amt in range(amount+1):
            if amt%coins[0]==0:
                dp[0][amt]=amt//coins[0]
            else:
                dp[0][amt]=1e9

        for i in range(1,n):
            for j in range(amount+1):
                #nottake 
                nottake=dp[i-1][j]    
                take=float('inf')
                if coins[i]<=j:
                    take=1+dp[i][j-coins[i]]

                dp[i][j]=min(nottake,take)    

        res=dp[n-1][amount]
        if res>=1e9:
            return -1

        return res        

