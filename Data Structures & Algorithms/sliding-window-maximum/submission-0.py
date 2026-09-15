from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq=deque()
        result=[]

        l=0
        for r in range(len(nums)):

            #remove out of window elements 
            while dq and dq[0]<=r-k:
                dq.popleft()

            
            #now for the current window we are going to build; remove anything smaller than current element so we maintain a monotonic deque 

            while dq and nums[dq[-1]]<=nums[r]:
                dq.pop()

            
            dq.append(r)

            if r-k>=-1:
                result.append(nums[dq[0]])
        
        return result


        