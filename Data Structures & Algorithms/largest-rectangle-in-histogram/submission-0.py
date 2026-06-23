class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #we can take a stack and for every index we can try to check whether we can form the largest rectangle using that bar 
        #for every bar, the area would be (height[i]*(width)) where width=nse_index-pse_index-1
        st=[]
        #so we are trying to make a monotonically inc stack 
        max_area=0
        n=len(heights)
        for i in range(n):
            while st and heights[st[-1]]>heights[i]:
                popped_element_nse=i
                popped_element_index=st.pop()
                popped_element_val=heights[popped_element_index]
                popped_element_pse=-1
                if st:
                    popped_element_pse=st[-1]
                area=popped_element_val * (popped_element_nse-popped_element_pse-1)
                max_area=max(area,max_area)

            st.append(i)

        while st:
            popped_element_nse=n
            popped_element_index=st.pop()
            popped_element_val=heights[popped_element_index]
            popped_element_pse=-1
            if st:
                popped_element_pse=st[-1]
            area=popped_element_val * (popped_element_nse-popped_element_pse-1)
            max_area=max(area,max_area)



        return max_area                

        