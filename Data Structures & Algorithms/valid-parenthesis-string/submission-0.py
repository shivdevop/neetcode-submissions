class Solution:
    def checkValidString(self, s: str) -> bool:
        st_brkt=[]
        st_star=[]
        
        for i in range(len(s)):
            if s[i]=='(':
                st_brkt.append(i)
            elif s[i]=='*':
                st_star.append(i)
            else:
                if st_brkt:
                    st_brkt.pop()
                elif st_star:
                    st_star.pop() 
                else:
                    return False

        while st_brkt:
            if not st_star or st_brkt[-1]>st_star[-1]:
                return False
            st_brkt.pop()
            st_star.pop()                           
        return True