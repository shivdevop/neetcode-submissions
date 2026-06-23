class Solution:
    def trap(self, height: List[int]) -> int:
        #lets store prefix max and suffix max 
        n=len(height)
        prefix_max_height=[0]*n
        prefix_height=0

        for i in range(n):
            prefix_max_height[i]=prefix_height
            prefix_height=max(prefix_max_height[i],height[i])

        suffix_max_height=[0]*n
        suffix_height=0
        for i in range(n-1,-1,-1):
            suffix_max_height[i]=suffix_height
            suffix_height=max(suffix_max_height[i],height[i])
        
        max_water_trapped=0
        for i in range(1,n-1):
            water_trap=min(prefix_max_height[i],suffix_max_height[i])-height[i]
            if water_trap>0:
                max_water_trapped+=water_trap

        return max_water_trapped                
        