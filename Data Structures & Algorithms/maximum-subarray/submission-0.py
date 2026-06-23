class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=0
        ms=float('-inf')

        for i in range(len(nums)):
            if cs<0:
                cs=0

            cs+=nums[i]
            ms=max(ms,cs)

        return ms        
        