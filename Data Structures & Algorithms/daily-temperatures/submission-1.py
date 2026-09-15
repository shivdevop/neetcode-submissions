class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)

        result=[0]*n
        st=[]

        for i,temp in enumerate(temperatures):

            while st and st[-1][0]<temp:
                    prev=st.pop()[1]
                    result[prev]=i-prev

            
            st.append((temp,i))
        
        return result
        