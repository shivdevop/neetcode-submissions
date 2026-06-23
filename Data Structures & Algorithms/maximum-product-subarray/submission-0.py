class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod,min_prod=1,1
        res=nums[0]
        for i in range(0,len(nums)):
            temp1=nums[i]*max_prod
            temp2=nums[i]*min_prod
            max_prod=max(temp1,temp2,nums[i])
            min_prod=min(temp1,temp2,nums[i])
            res=max(res,max_prod)

        return res    
        