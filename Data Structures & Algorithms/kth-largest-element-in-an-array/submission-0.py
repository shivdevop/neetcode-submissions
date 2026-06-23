
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap=[]
        i=0
        
        while i<k:
            heapq.heappush(min_heap,nums[i])
            i+=1
        #basically maintaining heap of size k
        while i<len(nums):
            heapq.heappushpop(min_heap,nums[i])
            i+=1


        return heapq.heappop(min_heap)    
