class Solution:
    def longestPalindrome(self, s: str) -> str:
        #we will traverse every index and every index we will consider it the center and try to expand it from center 
        res=None
        max_length=float('-inf')
        for i in range(len(s)):

            #odd length palindromic substr
            l,r=i,i
            res_l,res_r=None,None
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            res_l=l+1
            res_r=r
            if (res_r-res_l)>max_length:
                max_length=res_r-res_l
                res=s[res_l:res_r]

            #even_length
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            res_l=l+1
            res_r=r
            if (res_r-res_l)>max_length:
                max_length=res_r-res_l
                res=s[res_l:res_r]


        return res        


