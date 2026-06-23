from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        
        freq_map=defaultdict(int)
     
        for x in nums:
            freq_map[x]+=1

        map_of_freq=[[] for _ in range(n+1)]
        for val,freq in freq_map.items():
            map_of_freq[freq].append(val)
        
        res=[]
        for i in range(n,0,-1):
            for val in map_of_freq[i]:
                res.append(val)
                k-=1
                if k==0:
                    return res

        return res            


