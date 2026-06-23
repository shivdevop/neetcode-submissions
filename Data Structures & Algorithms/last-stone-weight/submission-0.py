import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[-1*stone for stone in stones]
        heapq.heapify(max_heap)

        while max_heap:
            if(len(max_heap)==1):
                break
            x=abs(heapq.heappop(max_heap))    
            y=abs(heapq.heappop(max_heap))
            if x==y:
                continue 
            heapq.heappush(max_heap,-1*(x-y))        
        
        if not max_heap:
            return 0
        return abs(heapq.heappop(max_heap))                