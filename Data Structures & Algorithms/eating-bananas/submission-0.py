import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles) #max i can eat the highest number of bananas pile in an hour
        
        def isPossible(bananas_per_hour):
            total_hours=0
            for bananas in piles:
                total_hours+=math.ceil(bananas/bananas_per_hour)

            if total_hours<=h:
                return True
            return False        




        min_eating_speed=None    
        while low<=high:
            mid=(low+high)//2
            if isPossible(mid):
                min_eating_speed=mid
                high=mid-1
            else:
                low=mid+1

        return min_eating_speed