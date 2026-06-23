class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxi=float('-inf')
        while i<j:
            area_water=min(heights[i],heights[j])*(j-i)
            maxi=max(maxi,area_water)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return maxi            
        