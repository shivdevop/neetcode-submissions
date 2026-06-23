class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if total%2!=0:
            return False
        
        target=total//2
        #find a subset with sum equal to target 

        dp=[[-1 for _ in range(target+1)]for _ in range(n)]

        def helper(ind,target):

            if ind==0:
                if nums[0]==target:
                    return 1
                elif target==0:
                    return 1 
                else:
                    return 0

            if dp[ind][target]!=-1:
                return dp[ind][target]            

            nottake=helper(ind-1,target)
            take=0
            if target>=nums[ind]:
                take=helper(ind-1,target-nums[ind])

            dp[ind][target]=take or nottake    


            return take or nottake       



        res=helper(n-1,target)
        return True if res==1 else False

