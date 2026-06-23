class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump=0
        for i in range(len(nums)):
            if i>max_jump:
                return False  #if i is not reachable 
            max_jump=max(max_jump,i+nums[i])

        return True    
