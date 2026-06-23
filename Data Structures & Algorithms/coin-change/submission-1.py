class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(n)]

        def helper(ind,target):
            if ind==0:
                if target==0:
                    return 0
                if target%coins[ind]==0:
                    return target//coins[0]
                else:
                    return 1e9    

            if dp[ind][target]!=-1:
                return dp[ind][target]        

            #nottake 
            nottake=helper(ind-1,target)    
            take=float('inf')
            if coins[ind]<=target:
                take=1+helper(ind,target-coins[ind])

            dp[ind][target]=min(nottake,take)    

            return min(nottake,take)

        res=helper(n-1,amount)
        if res>=1e9:
            return -1

        return res        

