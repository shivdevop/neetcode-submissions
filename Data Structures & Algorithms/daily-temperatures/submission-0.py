class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        n=len(temperatures)
        st=[]
        for i in range(n-1,-1,-1):
            while st and st[-1][0]<=temperatures[i]:
                st.pop()
            if st:
                nge_index=st[-1][1]
                res[i]=nge_index-i

            st.append((temperatures[i],i))

        return res         
        