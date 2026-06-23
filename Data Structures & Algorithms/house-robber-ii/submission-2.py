class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def helper(nums):
            n=len(nums)
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])

            prev=nums[0]
            curr=max(nums[0],nums[1])
            for i in range(2,n):
                temp=max(nums[i]+prev,curr)
                prev=curr
                curr=temp

            return curr    

        n=len(nums)
        return max(helper(nums[1:]),helper(nums[:n-1]))    

        