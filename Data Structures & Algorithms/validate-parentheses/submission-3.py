class Solution:
    def isValid(self, s: str) -> bool:
        mp={
            ']':'[',
            '}':'{',
            ')':'('
        }
        add=['(','{','[']
        st=[]

        for ch in s:
            if ch in add:
                st.append(ch)
            else: # ),},]
                if not st or (st and mp[ch]!=st[-1]):
                    return False
                elif st and mp[ch]==st[-1]:
                    st.pop()
                

        
        if not st:
            return True 
        return False
                