from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map=defaultdict(int)
        
        res=[[] for i in range(len(nums)+1)]

        for num in nums:
            freq_map[num]+=1

        
        for key,value in freq_map.items():
            res[value].append(key)

        ans=[]
        for i in range(len(res)-1,0,-1):
            for num in res[i]:
                ans.append(num)
                if len(ans)==k:
                    return ans
                
            







