from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map=defaultdict(int)

        for i,num in enumerate(nums):
            complement=target-num
            if complement in ind_map:
                return [ind_map[complement],i]
            ind_map[num]=i
        


        
        
        