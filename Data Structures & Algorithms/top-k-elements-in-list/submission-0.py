from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        max_heap=[]
        for val,freq in count.items():
            heapq.heappush(max_heap,(-freq,val))
        
        res=[]
        while k>0:
            freq,val=heapq.heappop(max_heap)
            res.append(val)
            k-=1
        return res        