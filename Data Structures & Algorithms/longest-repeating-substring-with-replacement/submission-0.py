class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map=[0]*26
        l,r=0,0
        max_freq=0
        max_len=0
        while r<len(s):
            ind=ord(s[r])-ord('A')
            freq_map[ind]+=1
            max_freq=max(max_freq,freq_map[ind])

            if (r-l+1) - max_freq>k:
                freq_map[ord(s[l])-ord('A')]-=1
                l+=1

            max_len=max(max_len,r-l+1)
            r+=1

        return max_len      
         