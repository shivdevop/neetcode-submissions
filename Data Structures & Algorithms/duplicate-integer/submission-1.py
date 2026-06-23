class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq_set=set(nums)
        if len(freq_set)<len(nums):
            return True 
        return False





        