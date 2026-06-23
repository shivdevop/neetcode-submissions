class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        
        def helper(ind,prev_ind):

            if ind==n:
                return 0

            if dp[ind][prev_ind+1] !=-1:
                return dp[ind][prev_ind+1]   

            nottake=helper(ind+1,prev_ind)
            take=float('-inf')
            if prev_ind==-1 or nums[ind]>nums[prev_ind]:
                take=1+helper(ind+1,ind)

            dp[ind][prev_ind+1]=max(take,nottake)    

            return max(nottake,take)            

        return helper(0,-1)


        