class Solution:
    def isValid(self, s: str) -> bool:
        match_map={
            "]":"[",
            "}":"{",
            ")":"("
        }

        st=[]
        
        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                st.append(s[i])
            elif not st or (st and match_map[s[i]]!=st[-1]):
                return False
            else:
                st.pop()

        if st:
            return False
        return True                

        