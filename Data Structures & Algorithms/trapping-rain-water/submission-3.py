class Solution:
    def trap(self, height: List[int]) -> int:

        # total_bars=len(height)

        # pre_max_heights=[0]*total_bars
        # post_max_heights=[0]*total_bars

        # pre_mh=height[0]
        # for i in range(1,total_bars):
        #     pre_max_heights[i]=pre_mh
        #     pre_mh=max(pre_mh,height[i])
        
        # #post max height
        # post_mh=height[total_bars-1]
        # for i in range(total_bars-2,-1,-1):
        #     post_max_heights[i]=post_mh
        #     post_mh=max(post_mh,height[i])

        # max_water=0
        # #now we have to iterate everybar and see if water can be stored there 

        # for i in range(1,total_bars-1):
        #     if pre_max_heights[i]>height[i]<post_max_heights[i]:
        #         max_water+=min(pre_max_heights[i],post_max_heights[i])-height[i]
        
        # return max_water
        total_bars=len(height)
        max_left,max_right=height[0],height[total_bars-1]
        l,r=0,total_bars-1

        max_water=0
        while l<r:
            if max_left<=max_right:
                l+=1
                if max_left>height[l]:
                    max_water+=(max_left-height[l])
                max_left=max(max_left,height[l])
            else:
                r-=1
                if max_right>height[r]:
                    max_water+=(max_right-height[r])
                max_right=max(max_right,height[r])
        
        return max_water


        