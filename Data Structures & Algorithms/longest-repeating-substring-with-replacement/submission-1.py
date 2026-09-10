class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        #count maintain 
        count=[0]*26 

        l=0
        longest=0
        max_freq=0


        for r in range(len(s)):
            idx=ord(s[r])-ord('A')
            count[idx]+=1

            max_freq=max(max_freq,count[idx])
            while (r-l+1)-max_freq>k:
                count[ord(s[l])-ord('A')]-=1
                l+=1
            
            longest=max(longest,r-l+1)
        
        return longest


        