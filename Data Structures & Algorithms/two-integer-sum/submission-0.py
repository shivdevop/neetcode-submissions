from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map=defaultdict(int)
        index_map[nums[0]]=0
        for i in range(1,len(nums)):
            if (target-nums[i]) in index_map and i!=index_map[target-nums[i]]:
                return [index_map[target-nums[i]],i]
            index_map[nums[i]]=i

        return [-1,-1]        
        